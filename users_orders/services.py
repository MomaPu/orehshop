from django.db import transaction
from django.http import request

from products.models import Products
from users_orders.models import Order


def add_product_to_cart(cart, product_id):

    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    return cart

def get_cart_data(cart):

    cart_items = []
    total_price = 0

    product_ids = [int(product_id_str) for product_id_str in cart.keys()]
    products = Products.objects.filter(pk__in=product_ids).prefetch_related('category')

    for product in products:
        quantity = cart[str(product.id)]
        cart_items.append({'product': product, 'quantity': quantity})
        total_price += product.price * quantity

    return {'cart_items': cart_items, 'total_price': total_price}


@transaction.atomic
def create_order_from_cart(user, cart_data):

    order = Order.objects.create(
        user=user,
        total_price=float(cart_data['total_price']),
    )


    for item in cart_data['cart_items']:
        product = item['product']
        order.products.add(product)
        product.stock -= item['quantity']
        product.save()

    return order

def clear_cart(request):

    request.session['cart'] = {}
    request.session.modified = True