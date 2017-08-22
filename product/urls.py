from django.conf.urls import include, url
from .import views

urlpatterns = [




   url(r'^$', views.index, name='index'),
    url(r'^ap/$', views.add_product, name='add_product'),

   #


]