#----class base -----
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
'''
The root of our API refers to 'user-list' and 'snippet-list'.
Our snippet serializer includes a field that refers to 'snippet-highlight'.
Our user serializer includes a field that refers to 'snippet-detail'.
Our snippet and user serializers include 'url' fields that by default will refer to 
'{model_name}-detail', which in this case will be 'snippet-detail' and 'user-detail'.
'''
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'contactInfomation',views.ContactInfomationViewSet)
router.register(r'contactAddress', views.ContactAddressViewSet)
router.register(r'questionType', views.QuestionTypeViewSet)
router.register(r'quickResultRecord', views.QuickResultRecordViewSet)
router.register(r'phoneConsultRecord', views.PhoneConsultRecordViewSet)
router.register(r'lawerToDoorRecord', views.LawerToDoorRecordViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'postInfo', views.PostInfoViewSet)
router.register(r'lawerLetterRecord', views.LawerLetterRecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
