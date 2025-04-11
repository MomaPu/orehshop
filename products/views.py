from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import ProductsFilterForm
from products.models import Products
from products.services import get_products


def home(request):
    form = ProductsFilterForm(request.GET or None)
    products = get_products()
    print("Request GET:", request.GET)
    filtered_products = products

    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)
    print("Filtered Products:", products)
    context = {'products': products, 'form': form}

    return render(request, 'main_page.html', context)

def product_detail(request, id):
    products_item = get_object_or_404(Products, id=id)
    return render(request, 'product_title.html', {'product': products_item})

def shop_info(request):
    pass
    return render(request, "shop_info.html")