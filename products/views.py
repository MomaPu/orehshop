from django.shortcuts import render

from products.forms import ProductsFilterForm
from products.services import get_product_with_reviews, get_filtered_products
from reviews.forms import ReviewForm


def get_homepage(request):
    form = ProductsFilterForm(request.GET or None)
    page_number = request.GET.get('page')
    filters = form.cleaned_data if form.is_valid() else {}

    page_obj = get_filtered_products(filters, page_number=page_number)


    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'main_page.html', {
        'form': form,
        'filter_params': filter_params.urlencode(),
        'page_obj': page_obj,
    })


def get_product_detail(request, id_product):

    page_number = request.GET.get('page')
    data = get_product_with_reviews(id_product, page_number)

    context = {
        'product': data['product'],
        'reviews': data['reviews'],
        'form': ReviewForm(),
    }
    return render(request, 'product_title.html', context)

