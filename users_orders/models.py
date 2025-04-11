from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model

class CartItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
	session_key = models.CharField(max_length=40, null=True, blank=True)  # Для анонимных пользователей

	def __str__(self):
		return f"{self.quantity} x {self.product.name}"

	def total_price(self):
		return self.quantity * self.product.price



