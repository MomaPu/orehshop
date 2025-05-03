from django.shortcuts import get_object_or_404

from products.models import Products
from reviews.models import Reviews


def create_product_review(product_id, user, data):
    product = get_object_or_404(Products, pk=product_id)

    if not data.get('text'):
        raise ValueError("Текст отзыва не может быть пустым.")

    review = Reviews.objects.create(product=product, user=user, text=data.get('text'))
    return review