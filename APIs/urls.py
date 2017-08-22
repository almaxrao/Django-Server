from django.conf.urls import include, url
from . import views

urlpatterns = [



    url(r'^pl/$', views.Product_list, name='Product_list'),



    url(r'^pd/(?P<pk>[0-9]+)/$', views.Product_detail ,name='Product_detail'),


]