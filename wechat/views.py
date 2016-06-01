# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from dbapi.models import Product
from wechat_info import WECHAT_TOKEN, AppID, AppSecret

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, ShortVideoMessage, VoiceMessage, EventMessage
from wechat_msg_deal import text_message_deal, video_message_deal, voice_message_deal, event_message_deal
from wechat_util import Sign
import json

# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)


@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        # 检验合法性
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # POST请求
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
    # 如果是发来的是文本信息
    if isinstance(wechat_instance.message, TextMessage):
        response = text_message_deal(wechat_instance)
    elif isinstance(wechat_instance.message, ShortVideoMessage):
        response = video_message_deal(wechat_instance)
    elif isinstance(wechat_instance.message, VoiceMessage):
        response = voice_message_deal(wechat_instance)
    elif isinstance(wechat_instance.message, EventMessage):
        response = event_message_deal(wechat_instance)
    return HttpResponse(response, content_type="application/xml")


def lawmall_index_view(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    # https://api.weixin.qq.com/sns/oauth2/access_token?appid=APPID&secret=SECRET&code=CODE&grant_type=authorization_code
    print code
    recommanded_products = Product.objects.filter(type=1)

    expert_products = Product.objects.filter(type=2)
    recommanded_products_title = recommanded_products[0].get_type_display()
    expert_products_title = recommanded_products[0].get_type_display()
    return render(request, 'wechat/index.html',
                  {'recommanded_products': recommanded_products,
                   'recommanded_products_title': recommanded_products_title,
                   'expert_products_title': expert_products_title, 'expert_products': expert_products})


def personal_view(request):
    return render(request, 'wechat/personal.html')


def product_detail_view(request, product_type, product_id):
    product = Product.objects.get(id=product_id)
    jsapi_ticket = wechat_instance.get_jsapi_ticket()['jsapi_ticket']
    app_id = AppID
    url = request.get_raw_uri()
    ret = Sign(jsapi_ticket=jsapi_ticket, url=url).sign()
    nonce_str = ret['nonceStr']
    timestamp = ret['timestamp']
    signature = ret['signature']

    print signature
    return render(request, 'wechat/product.html',
                  {'product': product, 'appId': json.dumps(app_id), 'timestamp': json.dumps(timestamp), 'nonceStr': json.dumps(nonce_str),
                   'signature': json.dumps(signature)})
