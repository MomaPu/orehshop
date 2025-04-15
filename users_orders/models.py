from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model

from users.models import User


class CartItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
	session_key = models.CharField(max_length=40, null=True, blank=True)  # Для анонимных пользователей

	def __str__(self):
		return f"{self.quantity} x {self.product.name}"

	def total_price(self):
		return self.quantity * self.product.price


class Order(models.Model):

	STATUS_CHOICES = [
		('pending', 'В обработке'),
		('shipped', 'Доставляется'),
		('delivered', 'Доставлен'),
		('canceled', 'Отменен'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
	total_price = models.DecimalField(max_digits=11, decimal_places=2)
	products = models.JSONField()

	def __str__(self):
		return f'Order {self.id} by {self.user.username} - Status: {self.status}'

