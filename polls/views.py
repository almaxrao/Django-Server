from django.shortcuts import render , redirect
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from django.template.context_processors import csrf

from .forms import ProductForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from .forms import ProfileForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")


#def index (request):
    #return render_to_response(request,'index.html')




class index(TemplateView):
   #template_name = 'product_listapi.html'
   template_name = 'logintest.html'


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request):
    return HttpResponse("You're voting on question " )







def update_profile(request):
 

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
           # messages.success(request, ('Your profile was successfully updated!'))
            return render_to_response(request,'success.html')
        #else:
           # messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def add_product (request):
    if request.POST:
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Added Successfully")
    else:
        form=ProductForm()

    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('add_product.html',args)








