# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import reverse, viewsets
from .models import ContactInformation
from .serializers import *

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactInfomationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerilizer


class ContactAddressViewSet(viewsets.ModelViewSet):
    queryset = ContactAddress.objects.all()
    serializer_class = ContactAddressSerilizer


class QuestionTypeViewSet(viewsets.ModelViewSet):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerilizer


class QuickResultRecordViewSet(viewsets.ModelViewSet):
    queryset = QuickResultRecord.objects.all()
    serializer_class = QuickResultRecordSerilizer


class PhoneConsultRecordViewSet(viewsets.ModelViewSet):
    queryset = PhoneConsultRecord.objects.all()
    serializer_class = PhoneConsultRecordSerilizer


class HighQualityContractRecordViewSet(viewsets.ModelViewSet):
    queryset = HighQualityContractRecord.objects.all()
    serializer_class = HighQualityContractRecordSerilizer


class LawerToDoorRecordViewSet(viewsets.ModelViewSet):
    queryset = LawerToDoorRecord.objects.all()
    serializer_class = LawerToDoorRecordSerilizer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizer


class PostInfoViewSet(viewsets.ModelViewSet):
    queryset = PostInfo.objects.all()
    serializer_class = PostInfoSerilizer


class LawerLetterRecordViewSet(viewsets.ModelViewSet):
    queryset = LawerLetterRecord.objects.all()
    serializer_class = LawerLetterRecordSerilizer
