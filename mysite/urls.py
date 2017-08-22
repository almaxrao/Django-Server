"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from restapp import views

urlpatterns = [
url(r'^polls/', include('polls.urls')),
     url(r'^admin/', admin.site.urls),
url(r'^user_login/', include('userlogging.urls')),
url(r'^user/', include('user.urls')),
url(r'^user_account/', include('userprofile.urls')),
    url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
url(r'^restapp/', include('restapp.urls')),
url(r'^api/', include('APIs.urls')),
url(r'^product/', include('product.urls')),
url(r'^cart/', include('cart.urls')),





   



]
