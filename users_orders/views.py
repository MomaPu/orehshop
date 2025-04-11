# products/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.http import HttpResponse

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id) #  Ключи в сессии должны быть строками!

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    request.session.modified = True  #  Обязательно! Говорит Django сохранить изменения

    #  Можно перенаправить обратно на страницу товара или на страницу корзины
    return redirect('home') #  или redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        product_id = int(product_id_str)
        try:
            product = Products.objects.get(pk=product_id)  # Обрабатываем случай, если товар удален
            cart_items.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity
        except Products.DoesNotExist:
            # Обрабатываем случай, если товара нет в базе (например, удалили)
            pass

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)
