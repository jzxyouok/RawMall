# -*- coding: utf-8 -*-
from wechat_info import MENU
from dbapi.models import User


def save_user_info(wechat_user_info):
    openid = wechat_user_info['openid']
    subscribe = wechat_user_info['subscribe']
    nickname = wechat_user_info['nickname']
    headimgurl = wechat_user_info['headimgurl']
    sex = wechat_user_info['sex']
    city = wechat_user_info['city']
    country = wechat_user_info['country']
    province = wechat_user_info['province']
    language = wechat_user_info['language']
    subscribe_time = wechat_user_info['subscribe_time']
    remark = wechat_user_info['remark']
    groupid = wechat_user_info['groupid']
    user = User.objects.create(openid=openid, subscribe=subscribe, nickname=nickname, headimgurl=headimgurl, city=city,
                               country=country, province=province, language=language, subscribe_time=subscribe_time,
                               remark=remark, groupid=groupid, sex=sex)
    user.save()


def delete_user_info(openid):
    user = User.objects.get(openid=openid)
    user.delete()


def voice_message_deal(wechat_instance):
    # 取得当前会话内容
    media_id = wechat_instance.message.media_id  # 对应于 XML 中的 MediaId
    format = wechat_instance.message.format  # 对应于 XML 中的 Format
    recognition = wechat_instance.message.recognition  # 对应于 XML 中的 Recognition
    reply_text = u'您发来一段语音' + format
    response = wechat_instance.response_text(content=reply_text)
    return response


def text_message_deal(wechat_instance):
    # 取得当前会话内容
    content = wechat_instance.message.content
    reply_text = u'您输入了' + content
    print wechat_instance.get_menu()
    response = wechat_instance.response_text(content=reply_text)
    return response


def video_message_deal(wechat_instance):
    # 取得当前会话内容
    media_id = wechat_instance.message.media_id  # 对应于 XML 中的 MediaId
    thumb_media_id = wechat_instance.message.thumb_media_id  # 对应于 XML 中的 ThumbMediaId
    reply_text = u'您发来一段小视频' + media_id
    response = wechat_instance.response_text(content=reply_text)
    return response


def event_message_deal(wechat_instance):
    # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
    if wechat_instance.message.type == 'subscribe':
        key = wechat_instance.message.key  # 对应于 XML 中的 EventKey (普通关注事件时此值为 None)
        ticket = wechat_instance.message.ticket  # 对应于 XML 中的 Ticket (普通关注事件时此值为 None)
        reply_text = u'用户关注了'
        user_id = wechat_instance.message.source
        wechat_user_info = wechat_instance.get_user_info(user_id, lang='zh_CN')
        # 保存用户信息到数据库
        save_user_info(wechat_user_info)
        response = wechat_instance.response_text(content=reply_text)
        return response
    # 取消关注事件（无可用私有信息）
    elif wechat_instance.message.type == 'unsubscribe':
        print u'用户取消了关注'
        delete_user_info(wechat_instance.message.source)
        reply_text = u'用户取消了关注'

        response = wechat_instance.response_text(content=reply_text)
        return response
    # 用户已关注时的二维码扫描事件
    elif wechat_instance.message.type == 'scan':
        key = wechat_instance.message.key  # 对应于 XML 中的 EventKey
        ticket = wechat_instance.message.ticket  # 对应于 XML 中的 Ticket
    # 上报地理位置事件
    elif wechat_instance.message.type == 'location':
        latitude = wechat_instance.message.latitude  # 对应于 XML 中的 Latitude
        longitude = wechat_instance.message.longitude  # 对应于 XML 中的 Longitude
        precision = wechat_instance.message.precision  # 对应于 XML 中的 Precision
    # 自定义菜单点击事件
    elif wechat_instance.message.type == 'click':
        key = wechat_instance.message.key  # 对应于 XML 中的 EventKey

    # 自定义菜单跳转链接事件
    elif wechat_instance.message.type == 'view':
        key = wechat_instance.message.key  # 对应于 XML 中的 EventKey
    # 模板消息事件
    elif wechat_instance.message.type == 'templatesendjobfinish':
        status = wechat_instance.message.status  # 对应于 XML 中的 Status
    elif wechat_instance.message.type in ['scancode_push', 'scancode_waitmsg', 'pic_sysphoto',
                                          'pic_photo_or_album', 'pic_weixin', 'location_select']:  # 其他事件
        key = wechat_instance.message.key  # 对应于 XML 中的 EventKey
