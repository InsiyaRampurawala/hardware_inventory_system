from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    related_products = Product.objects.exclude(id=id)[:4]

    return render(request, "product_detail.html", {
        "product": product,
        "related_products": related_products
    })