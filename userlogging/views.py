from django.shortcuts import render , render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
      #return render_to_response('product_listapi.html', request)
      return render(request, 'product_listapi.html')


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/user_login/loggedin')
    else:
        return HttpResponseRedirect('/user_login/invalid')

def loggedin (request):
    return  render_to_response('loggedin.html',{'full_name' : request.user.username})  #this full name is the variable that we have used in loggedin.html file

def invalid_login (request):
    return render_to_response('invalid_login.html')

def logout (request):
    auth.logout(request)
    return render_to_response('login.html')


def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return render_to_response('register_success.html')
            return HttpResponseRedirect('/user_login/register_success')
        else:
            return HttpResponseRedirect('/user_login/invalid')


    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    return render_to_response('register.html' ,args)


def register_success(request):
    return render_to_response('register_success.html')