from django.contrib import admin

from products.models import Products, Category, Information

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Information)