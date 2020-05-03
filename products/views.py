from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Model, Offer


# Create your views here.


def product(request):
    products = Model.objects.all()
    return render(request, 'index.html', {'products': products})


def newProduct(request):
    return HttpResponse('new product page')
