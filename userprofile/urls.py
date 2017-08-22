from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^profile/$', views.user_profile , name='userprofile'),


]