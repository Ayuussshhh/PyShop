from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
# Uniform Resource Locator (Address)

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products' : product})

def new(request):
    return HttpResponse('Hi! It is so good to see you.')

