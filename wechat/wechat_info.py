# -*- coding: utf-8 -*-
"""
本模块存储微信的静态变量
"""
# 微信基本配置信息
WECHAT_TOKEN = 'wechat'
AppID = 'wx6fdfb74343926922'
AppSecret = '8c8d81d7bdf289335a85aec015eb8186'

# 公众号自定义菜单,json格式
MENU = {
    "button": [
        {
            "name": "快速体验",
            "sub_button": [
                {
                    "type": "click",
                    "name": "免费快速咨询",
                    "key": "FREE_QUICK_CONSULT"
                },
                {
                    "type": "view",
                    "name": "免费电话咨询",
                    "url": "http://14907eb226.imwork.net/wechat/"
                },
                {
                    "type": "view",
                    "name": "精品合同",
                    "url": "http://14907eb226.imwork.net/wechat/"
                },
                {
                    "type": "view",
                    "name": "律师函",
                    "url": "http://14907eb226.imwork.net/wechat/"
                },
                {
                    "type": "view",
                    "name": "律师上门",
                    "url": "http://14907eb226.imwork.net/wechat/"
                }
            ]
        },
        {
            "type": "view",
            "name": "法律商城",
            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx6fdfb74343926922&redirect_uri=http%3A%2F%2F14907eb226.imwork.net%2Fwechat%2Findex&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect"
        },
        {
            "name": "我",
            "sub_button": [
                {
                    "type": "view",
                    "name": "个人主页",
                    "url": "http://14907eb226.imwork.net/wechat/"
                },
                {
                    "type": "view",
                    "name": "我的订单",
                    "url": "http://14907eb226.imwork.net/wechat/"
                },
                {
                    "type": "click",
                    "name": "购买历史",
                    "key": "V1001_GOOD"
                }
            ]
        }
    ]
}