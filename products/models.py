from django.db import models

class Category(models.Model):

	name = models.CharField("Наименование", max_length=100, unique=True)

	def __str__(self):
		return self.name

class Products(models.Model):

	name = models.CharField("Название", max_length=64, unique=True)
	price = models.DecimalField("Стоимость", max_digits=12, decimal_places=2)
	text = models.TextField("Описание")
	stock = models.IntegerField(default=0)
	image = models.ImageField("Изображение", upload_to='images/', null=True, blank=True)
	category = models.ManyToManyField(Category, verbose_name="Категории")

	def __str__(self):
		return self.name

