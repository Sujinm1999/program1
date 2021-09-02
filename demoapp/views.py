from django.shortcuts import render ,get_object_or_404,redirect
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.models import User,auth

# Create your views here.

def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    pro=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category=c_page,available=True)

    else:
        products=Product.objects.all().filter(available=True)
    paginator=Paginator(products,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':pro})

def ProdCatDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
