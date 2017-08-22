from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [


    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index.as_view(), name='index'),

    url(r'^with_login/$', views.with_login, name='with_login'),
    url(r'^without_login/$', views.without_login, name='without_login'),

   #url(r'^at/(?P<pk>[0-9]+)/$', views. AddtoCart ,name=' AddtoCart'),

   # url(r'^ac/$', views.add_cart, name='add_cart'),

    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    


    






  


]