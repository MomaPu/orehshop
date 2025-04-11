from django.contrib.auth.models import AbstractUser
from django.db import models

class Address(models.Model):
    street_address = models.CharField(max_length=255, verbose_name="Улица и номер дома")
    city = models.CharField(max_length=100, verbose_name="Город")
    state = models.CharField(max_length=100, blank=True, verbose_name="Область/Регион")
    postal_code = models.CharField(max_length=20, verbose_name="Почтовый индекс")
    country = models.CharField(max_length=100, verbose_name="Страна")

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.postal_code}"

class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Адрес")

    def __str__(self):
        return self.username