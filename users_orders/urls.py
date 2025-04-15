from django.urls import path
from . import views
from .views import create_order, user_orders

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('create-order/', create_order, name='create_order'),
    path('my-orders/', user_orders, name='users_orders')
]

