from django.contrib import admin

from products.models import Products, Category

admin.site.register(Products)
admin.site.register(Category)
