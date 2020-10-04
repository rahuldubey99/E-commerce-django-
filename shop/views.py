from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    print(" \n pro \n  ",products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    parms = {'no_of_slides':nSlides, 'range' : range(nSlides),'product': products}
    return render(request,"shop/index.html", parms)



def About(request):
    return render(request, 'shop/about.html')
def Tracker(request):
    return HttpResponse("Tracker")
def Contact(request):
    return HttpResponse("Conntact")
def Search(request):
    return HttpResponse("Search")
def Productview(request):
    return HttpResponse("ProductView")
def Checkout(request):
    return HttpResponse("Checkout")
