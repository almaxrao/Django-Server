from django.shortcuts import render




# Create your views here.


from .forms import ProductForm
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




#@login_required
def index(request):
      #return render_to_response('product_listapi.html', request)
      return render(request, 'product_listapi.html')


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