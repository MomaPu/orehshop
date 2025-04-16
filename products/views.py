from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import ProductsFilterForm, ReviewForm
from products.models import Products, Information
from products.services import get_products

def home(request):
    form = ProductsFilterForm(request.GET or None)
    products = get_products()
    products = products.distinct()

    if request.GET:
        if form.is_valid():
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            categories = form.cleaned_data.get('category')

            if min_price:
                products = products.filter(price__gte=min_price)
            if max_price:
                products = products.filter(price__lte=max_price)
            if categories:
                products = products.filter(category__in=categories)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    filter_params = request.GET.copy()  # Создаем копию GET параметров
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'main_page.html', {'form': form, 'page_obj': page_obj,
                                              'filter_params': filter_params.urlencode()})


def product_detail(request, id_product):
    product = get_object_or_404(Products, id=id_product)
    reviews = product.reviews.all().order_by('-created_at')

    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'product': product,
        'reviews': page_obj,
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
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', id_product=product.id)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product_detail.html', context)