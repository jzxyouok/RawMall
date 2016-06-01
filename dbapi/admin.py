# -*- coding: utf-8 -*-
from django.contrib import admin
from dbapi.models import *


# 自定义后台展现
class MyAdminSite(admin.AdminSite):
    site_header = u'法律商城    微信后台'
    index_title = u'顶部名称'


admin_site = MyAdminSite(name='myadmin')


class ContactAddressAdmin(admin.StackedInline):
    model = ContactAddress
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ('openid', 'nickname', 'sex', 'country', 'province', 'city',
                    'language', 'subscribe_time', 'remark', 'groupid',)
    search_fields = ('nickname', 'sex',)
    # fields = ( 'remark', 'groupid',)
    ordering = ('subscribe_time',)
    fieldsets = [
        (u'基本信息', {'fields': ['nickname', 'sex', ]}),
        ('Date information', {'fields': ['subscribe_time']}),
    ]
    inlines = [ContactAddressAdmin]


admin_site.register(User, UserAdmin)

# class ContactAddressAdmin(admin.ModelAdmin):
#     list_display = ('user', 'country', 'province', 'city')
#     search_fields = ('user',)
#     # inlines = [UserAdmin]
#     raw_id_fields = ('user',)



# admin_site.register(ContactAddress, ContactAddressAdmin)


class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_name')
    search_fields = ('type_code', 'type_name')


admin_site.register(QuestionType, QuestionTypeAdmin)


class QuickResultRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_time', 'question_description')
    search_fields = ('user', 'create_time', 'question_description')


admin_site.register(QuickResultRecord, QuickResultRecordAdmin)


class PhoneConsultRecordAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'create_time', 'question_description', 'question_type', 'question_picture1', 'question_picture2')
    search_fields = ('user', 'question_description')


admin_site.register(PhoneConsultRecord, PhoneConsultRecordAdmin)


class HighQualityContractRecordAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'create_time', 'requirement', 'question_type', 'question_picture1', 'question_picture2', 'phone',
        'email')
    search_fields = ('user', 'create_time',)


admin_site.register(HighQualityContractRecord, HighQualityContractRecordAdmin)


class LawerToDoorRecordAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'create_time', 'question_description', 'to_door_address', 'to_door_time', 'question_type',
        'contact_info')
    search_fields = ('user', 'create_time', 'question_description')


admin_site.register(LawerToDoorRecord, LawerToDoorRecordAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price', 'introduction', 'customer')
    search_fields = ('name', 'price', 'introduction', 'customer')


admin_site.register(Product, ProductAdmin)


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'iconfont', 'item', 'desc')
    search_fields = ('desc', 'desc')


admin_site.register(ProductDetail, ProductDetailAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_time', 'status', 'payment_type', 'count', 'money')
    # , 'product'
    search_fields = ('user', 'create_time',)
    filter_horizontal = ('product',)
    date_hierarchy = 'create_time'


admin_site.register(Order, OrderAdmin)


class PostInfoAdmin(admin.ModelAdmin):
    list_display = (
        'sender_name', 'sender_contact_info', 'sender_address', 'sender_company', 'sender_postcode', 'receiver_name',
        'receiver_contact_info', 'receiver_address', 'receiver_company', 'receiver_postcode')
    search_fields = ('sender_name', 'receiver_name')


admin_site.register(PostInfo, PostInfoAdmin)


class LawerLetterRecordAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'create_time', 'question_description', 'question_type', 'question_picture1', 'question_picture2',
        'post_way', 'post_info', 'contact_info')
    search_fields = ('user', 'create_time', 'question_description')


admin_site.register(LawerLetterRecord, LawerLetterRecordAdmin)
