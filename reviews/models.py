from django.db import models

class Reviews(models.Model):
	product = models.ForeignKey('products.Products', related_name='reviews', on_delete=models.CASCADE)
	text = models.TextField('Текст отзыва')
	user = models.ForeignKey('users.User', related_name='user_reviews', null=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	rating = models.IntegerField(default=5, verbose_name='Рейтинг', choices=[(i, i) for i in range(1, 6)])

