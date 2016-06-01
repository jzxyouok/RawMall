# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    SEX = ((1, u'男'), (2, u'女'), (0, u'未知'))
    SUBSCRIBE = ((1, u'已关注'), (0, u'未关注'))
    LANGUAGE = (('zh_CN', U'简体中文'),)

    subscribe = models.IntegerField(choices=SUBSCRIBE, verbose_name=u'是否已关注')
    openid = models.CharField(max_length=100, primary_key=True, verbose_name='微信openid')
    nickname = models.CharField(max_length=100, verbose_name=u'用户昵称')
    headimgurl = models.CharField(max_length=150, verbose_name=u'用户头像')
    sex = models.IntegerField(choices=SEX, verbose_name=u'性别')
    city = models.CharField(max_length=20, verbose_name=u'城市')
    country = models.CharField(max_length=20, verbose_name=u'国家')
    province = models.CharField(max_length=20, verbose_name=u'省份')
    language = models.CharField(max_length=20, verbose_name=u'语言', choices=LANGUAGE)
    subscribe_time = models.IntegerField(verbose_name=u'关注时间')
    remark = models.CharField(max_length=30, verbose_name=u'对粉丝的备注')
    groupid = models.IntegerField(verbose_name=u'分组ID')

    def __unicode__(self):
        return '%s' % self.nickname

    class Meta:
        managed = True
        ordering = ('subscribe_time',)
        db_table = 't_user'
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class ContactInformation(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    phone = models.CharField(max_length=100, verbose_name=u'电话')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = u't_contact_information'
        verbose_name = u'联系方式'
        verbose_name_plural = u'联系方式'


class ContactAddress(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    country = models.CharField(max_length=100, verbose_name=u'国家')
    province = models.CharField(max_length=100, verbose_name=u'省')
    city = models.CharField(max_length=100, verbose_name=u'城市')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = u't_contact_address'
        verbose_name = u'联系地址'
        verbose_name_plural = u'联系地址'


class QuestionType(models.Model):
    type_code = models.IntegerField(primary_key=True, verbose_name=u'类型编号')
    type_name = models.CharField(max_length=100, verbose_name=u'类型值')

    class Meta:
        managed = True
        ordering = ('type_code',)
        db_table = 't_question_type'
        verbose_name = u'问题类型'
        verbose_name_plural = u'问题类型'


class QuickResultRecord(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'询问时间')
    question_description = models.CharField(max_length=200, verbose_name=u'问题描述')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = 't_quick_result_record'
        verbose_name = u'快速咨询记录'
        verbose_name_plural = u'快速咨询记录'


class PhoneConsultRecord(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'询问时间')
    question_description = models.CharField(max_length=200, verbose_name=u'问题描述')
    question_type = models.ForeignKey(QuestionType, verbose_name=u'问题类型')
    question_picture1 = models.CharField(max_length=100, verbose_name=u'问题图片1')
    question_picture2 = models.CharField(max_length=100, verbose_name=u'问题图片2')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = 't_phone_consult_record'
        verbose_name = u'电话咨询记录'
        verbose_name_plural = u'电话咨询记录'


class HighQualityContractRecord(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    requirement = models.CharField(max_length=200, verbose_name=u'要求')
    question_type = models.ForeignKey(QuestionType, verbose_name=u'问题类型')
    question_picture1 = models.CharField(max_length=100, verbose_name=u'问题图片1')
    question_picture2 = models.CharField(max_length=100, verbose_name=u'问题图片2')
    phone = models.CharField(max_length=100, verbose_name=u'电话')
    email = models.EmailField(verbose_name=u'电子邮件')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = 't_high_quality_contract_record'
        verbose_name = u'电话咨询记录'
        verbose_name_plural = u'电话咨询记录'


class LawerToDoorRecord(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    question_description = models.CharField(max_length=200, verbose_name=u'问题描述')
    to_door_address = models.CharField(max_length=200, verbose_name=u'上门地址')
    to_door_time = models.DateTimeField
    question_type = models.ForeignKey(QuestionType, verbose_name=u'问题类型')
    contact_info = models.CharField(max_length=200, verbose_name=u'联系信息')

    class Meta:
        managed = True
        ordering = ('user',)
        db_table = 't_lawer_to_door_record'
        verbose_name = u'律师上门记录'
        verbose_name_plural = u'律师上门记录'


class Product(models.Model):
    ICONFONTS = ((u'xe635;', u'笑脸'), (u'xe600;', u'电话'), (u'xe705;', u'合同'))
    TYPE = ((1, u'推荐类法律顾问'), (2, u'专家类法律顾问'))
    id = models.IntegerField(primary_key=True, verbose_name=u'序号')
    iconfont = models.CharField(choices=ICONFONTS, max_length=20, verbose_name=u'详情图标', default=u'xe635;')
    name = models.CharField(max_length=100, verbose_name=u'产品名')
    type = models.IntegerField(choices=TYPE, verbose_name=u'产品类型', default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u'价格')
    customer = models.CharField(max_length=50, verbose_name=u'目标人群', null=True, blank=True)
    introduction = models.CharField(max_length=200, verbose_name=u'简介')

    def __unicode__(self):
        return u'%d %s' % (self.id, self.name)

    class Meta(object):
        db_table = 't_product'
        ordering = ('id', 'price',)
        managed = True
        verbose_name = u'产品'
        verbose_name_plural = u'产品'


class ProductDetail(models.Model):
    ICONFONTS = ((u'xe635;', u'笑脸'), (u'xe600;', u'电话'), (u'xe705;', u'合同'))

    product = models.ForeignKey(Product)
    iconfont = models.CharField(choices=ICONFONTS, max_length=20, verbose_name=u'分点图标')
    item = models.CharField(max_length=20, verbose_name=u'分点')
    desc = models.CharField(max_length=100, verbose_name=u'分点描述')

    class Meta:
        managed = True
        verbose_name = u'产品分点详情'
        verbose_name_plural = u'产品分点详情'
        db_table = 't_product_detail'


class Order(models.Model):
    STATUS = (('1', u'未确认'),
              ('2', u'处理中'),
              ('3', u'被拒绝'),
              ('4', u'已处理'))
    PAYMENt_TYPE = (
        ('1', u'支付宝'),
        ('2', u'微信支付'),
        ('3', u'财付通'),
        ('4', u'银行卡'),
    )
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(verbose_name=u'创建时间')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'订单状态')
    payment_type = models.CharField(max_length=1, choices=PAYMENt_TYPE, verbose_name=u'支付方式')
    count = models.IntegerField(verbose_name=u'数量')
    money = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u'总价')
    product = models.ManyToManyField(Product, verbose_name=u'产品')

    class Meta(object):
        ordering = ('-create_time',)
        managed = True
        verbose_name = u'订单'
        verbose_name_plural = u'订单'
        db_table = 't_order'


# class OrderDetail(models.Model):
#     product_id = models.CharField(max_length = 100)
#     order_id = models.CharField(max_length = 100)


class PostInfo(models.Model):
    sender_name = models.CharField(max_length=100, verbose_name=u'寄件人')
    sender_contact_info = models.CharField(max_length=100, verbose_name=u'手机')
    sender_address = models.CharField(max_length=100, verbose_name=u'地址')
    sender_company = models.CharField(max_length=100, null=True, verbose_name=u'公司')
    sender_postcode = models.CharField(max_length=100, null=True, verbose_name=u'邮编')
    receiver_name = models.CharField(max_length=100, verbose_name=u'收件人')
    receiver_contact_info = models.CharField(max_length=100, verbose_name=u'手机')
    receiver_address = models.CharField(max_length=100, verbose_name='地址')
    receiver_company = models.CharField(max_length=100, null=True, verbose_name=u'公司')
    receiver_postcode = models.CharField(max_length=100, null=True, verbose_name=u'邮编')

    class Meta(object):
        managed = True
        verbose_name = u'邮寄信息'
        verbose_name_plural = u'邮寄信息'
        db_table = 't_post_info'


class LawerLetterRecord(models.Model):
    POSt_WAY = (
        ('1', u'寄给我'),
        ('2', u'帮我寄')
    )
    user = models.ForeignKey(User, verbose_name=u'用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    question_description = models.CharField(max_length=200, verbose_name=u'问题描述')
    question_type = models.ForeignKey(QuestionType, verbose_name=u'问题类型')
    question_picture1 = models.CharField(max_length=100, verbose_name=u'问题照片1')
    question_picture2 = models.CharField(max_length=100, verbose_name=u'问题照片1')
    post_way = models.CharField(max_length=1, choices=POSt_WAY, verbose_name=u'邮寄方式')
    post_info = models.ForeignKey(PostInfo, verbose_name=u'邮寄信息')
    contact_info = models.CharField(max_length=100, verbose_name=u'手机')

    class Meta(object):
        ordering = ('-create_time',)
        managed = True
        verbose_name = u'律师函记录'
        verbose_name_plural = u'律师函记录'
        db_table = 't_lawer_letter_record'


# 微信号自定义菜单类
class Menu(models.Model):
    pass
