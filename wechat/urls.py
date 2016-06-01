from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
    # url(r'^$', views.WechatInterfaceView.as_view()),
    url(r'^$', views.index),
    url(r'^index/$', views.lawmall_index_view,name='index'),
    url(r'^index/personal$', views.personal_view, name='personal'),
    url(r'^detail/(\d+)/(\d+)/$', views.product_detail_view, name='product_detail'),



]