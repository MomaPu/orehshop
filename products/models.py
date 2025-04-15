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


class Information(models.Model):
	text = models.TextField("Информация")
	def __str__(self):
		return self.text


class Reviews(models.Model):
	product = models.ForeignKey('Products', related_name='reviews', on_delete=models.CASCADE)
	text = models.TextField('Текст отзыва')
	user = models.ForeignKey('users.User', related_name='user_reviews', null=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	rating = models.IntegerField(default=5, verbose_name='Рейтинг', choices=[(i, i) for i in range(1, 6)])

