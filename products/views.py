from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from information.models import Information
from products.forms import ProductsFilterForm
from products.models import Products
from products.services import get_product_with_reviews, get_filtered_products, create_product_review
from reviews.forms import ReviewForm


def home(request):
    form = ProductsFilterForm(request.GET or None)
    products = get_filtered_products(form.cleaned_data if form.is_valid() else {})

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'main_page.html', {'form': form, 'page_obj': page_obj,
                                              'filter_params': filter_params.urlencode()})


def product_detail(request, id_product):

    product = get_object_or_404(Products, id=id_product)
    page_number = request.GET.get('page')
    data = get_product_with_reviews(product.id, page_number)

    context = {
        'product': data['product'],
        'reviews': data['reviews'],
        'form': ReviewForm(),
    }
    return render(request, 'product_title.html', context)

def shop_info(request):
    info = Information.objects.all()
    context = {
        'info': info
    }
    return render(request, "shop_info.html", context)

@login_required
def create_review(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            create_product_review(product_id, request.user, form.cleaned_data)
            return redirect(reverse('product_detail', kwargs={'id_product': product_id}))
        else:
            context = {
            'product': product,
            'form': form,
            }
            return render(request, 'product_title.html', context)
    else:
        form = ReviewForm()
        context = {
            'product': product,
            'form': form,
            }
        return render(request, 'product_title.html', context)