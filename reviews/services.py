from django.shortcuts import get_object_or_404

from products.models import Products
from reviews.models import Reviews


def create_product_review(product_id, user, data):

    product = get_object_or_404(Products, pk=product_id)
    review = Reviews.objects.create(product_id=product.id, author=user, text=data.get('text')) # Используем create
    return review