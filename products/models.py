from django.db import models

class Products(models.Model):

	name = models.CharField("Название", max_length=64, unique=True)
	price = models.DecimalField("Стоимость", max_digits=12, decimal_places=2)
	text = models.TextField("Описание")
	stock = models.IntegerField(default=0)
	image = models.ImageField("Изображение", upload_to='images/', null=True, blank=True)
