# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('openid', 'wechat_id', 'wechat_nickname', 'wechat_picture',
                  'nickname', 'picture', 'gender', 'language', 'attach_time')


class ContactInformationSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ContactInformation
        fields = ('user', 'phone')


class ContactAddressSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ContactAddress
        fields = ('user', 'country', 'province', 'city')


class QuestionTypeSerilizer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        fields = ('type_code', 'type_name')


class QuickResultRecordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = QuickResultRecord
        fields = ('user', 'create_time', 'question_description')


class PhoneConsultRecordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = PhoneConsultRecord
        fields = ('user', 'create_time', 'question_description',
                  'question_type', 'question_picture1', 'question_picture2')


class HighQualityContractRecordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = HighQualityContractRecord
        fields = ('user', 'create_time', 'requirement', 'question_type',
                  'question_picture1', 'question_picture2', 'phone', 'email')


class LawerToDoorRecordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = LawerToDoorRecord
        fields = ('user', 'create_time', 'question_description',
                  'question_type', 'to_door_address', 'to_door_time', 'contact_info')


class ProductSerilizer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    introduction = serializers.CharField(max_length=200)
    class Meta:
        model = Product
        fields = ('name', 'price', 'introduction')


class OrderSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('user', 'create_time', 'status',
                  'payment_type', 'count', 'money', 'product')


class PostInfoSerilizer(serializers.ModelSerializer):

    class Meta:
        model = PostInfo
        fields = ('sender_name', 'sender_contact_info', 'sender_address', 'sender_company', 'sender_postcode',
                  'receiver_name', 'receiver_contact_info', 'receiver_address', 'receiver_company', 'receiver_postcode')


class LawerLetterRecordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = LawerLetterRecord
        fields = ('user', 'create_time', 'question_description', 'question_type', 'question_picture1', 'question_picture2',
                  'post_way', 'post_info', 'contact_info')
