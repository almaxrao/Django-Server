from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
#from .models import Cart
#from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from django.template.context_processors import csrf


from .forms import *
# Create your views here.

class index(TemplateView):
   #template_name = 'product_listapi.html'
   template_name = 'logintest.html'


@login_required
def with_login(request):
       return HttpResponse("You came here by successfully logging in")

def without_login(request):
       return HttpResponse("You came here without logging in")


def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Suuccessful Registration")
        else:
            return HttpResponse("Invalid Registration")
    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request,'registration/register.html', args)


'''
@api_view(['GET', 'PUT', 'DELETE'])
def AddtoCart(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Cart.objects.get(pk=pk)

    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(task)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(task, data=request.DATA)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@login_required
def add_cart (request):
    if request.method == 'POST':

        profile_form = CartForm(request.POST, instance=request.user.profile)
        if  profile_form.is_valid():

            profile_form.save()
            return HttpResponseRedirect('/user_login/loggedin')
        else:
            HttpResponse("Error")
    else:

        profile_form = CartForm(instance=request.user.profile)
    return render(request, 'cartapi.html', {

        'profile_form': profile_form
    })
'''