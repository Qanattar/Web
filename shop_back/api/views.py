from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
import json
from api.models import Product, Category


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return JsonResponse(product.to_json())


def category(request):
    categories = Category.objects.all()
    categories_json = [cat.to_json() for cat in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    cat = Category.objects.get(id=category_id)
    return JsonResponse(cat.to_json())


def product_category(request, category_id):
    cat = Category.objects.get(id=category_id)
    product = Product.objects.get(description="")
    return JsonResponse(product.to_json())
