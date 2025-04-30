from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .models import Order
from .services import add_product_to_cart, get_cart_data, create_order_from_cart, clear_cart


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart = add_product_to_cart(cart, product_id)

    request.session['cart'] = cart
    request.session.modified = True


    return redirect('home')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_data = get_cart_data(cart)

    context = {'cart_items': cart_data['cart_items'], 'total_price': cart_data['total_price']}
    return render(request, 'cart.html', context)


def create_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return render(request, 'cart.html', {'message': 'Корзина пуста'})

    cart_data = get_cart_data(cart)

    if request.method == "POST":
        order = create_order_from_cart(request.user, cart_data)
        clear_cart(request)

        return redirect('user_profile')

    return render(request, 'create_order.html')

def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'users_orders.html', context)

