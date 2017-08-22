from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login

urlpatterns = [



   
    url(r'^profile/$', views.update_profile, name='update_profile'),





    url(r'^$', views.index.as_view(), name='index'),





    


    






  

    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^vote/$', views.vote, name='vote'),

]