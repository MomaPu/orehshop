from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from products.models import Products



def get_product_with_reviews(product_id, page_number=1, reviews_per_page=5):
    product = get_object_or_404(Products, id=product_id)
    reviews = product.reviews.all().order_by('-created_at')

    paginator = Paginator(reviews, reviews_per_page)
    page_obj = paginator.get_page(page_number)

    return {'product': product, 'reviews': page_obj}

def get_filtered_products(filters, page_number=1, products_per_page=6):

    products = Products.objects.all()


    if filters.get('min_price'):
        products = products.filter(price__gte=filters['min_price'])
    if filters.get('max_price'):
        products = products.filter(price__lte=filters['max_price'])
    if filters.get('categories'):
        products = products.filter(category__in=filters['categories'])

    paginator = Paginator(products, products_per_page)
    page_obj = paginator.get_page(page_number)

    return page_obj


