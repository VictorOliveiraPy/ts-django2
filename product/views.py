from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def product(request):
    return render(request, 'product/product.html')


def create_product(request):
    return render(request, 'product/create.html')


def category(request):
    return render(request, 'product/category.html')


def create_category(request):
    return render(request, 'product/create_category.html')