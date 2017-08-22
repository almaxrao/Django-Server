from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^ac/$', views.user_cart , name='user_cart'),


]