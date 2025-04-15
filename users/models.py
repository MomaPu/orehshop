from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    def __str__(self):
        return self.username

class Support(models.Model):
    mail = models.TextField("Почта", max_length=64)
    text = models.TextField("Текст сообщения  ")
