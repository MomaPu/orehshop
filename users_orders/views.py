# products/views.py
from django.shortcuts import render, redirect
from .models import Products, Order


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    request.session.modified = True


    return redirect('home')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        product_id = int(product_id_str)
        try:
            product = Products.objects.get(pk=product_id)
            cart_items.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity
        except Products.DoesNotExist:
            pass

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)


def create_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return render(request, 'cart.html', {'message': 'Корзина пуста'})

    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        product_id = int(product_id_str)
        try:
            product = Products.objects.get(pk=product_id)

            cart_items.append({
                'product_id': product.id,  # Сохраняем id продукта
                'name': product.name,  # Сохраняем название продукта
                'quantity': quantity,  # Сохраняем количество
                'price': str(product.price)  # Преобразуем Decimal в строку
            })
            total_price += product.price * quantity
        except Products.DoesNotExist:
            continue

    if request.method == "POST":

        order = Order.objects.create(
            user=request.user,
            total_price=float(total_price),  # Преобразуем Decimal в float
            products=cart_items
        )

        request.session['cart'] = {}
        request.session.modified = True

        return redirect('user_profile')

    return render(request, 'create_order.html')


def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'users_orders.html', context)

