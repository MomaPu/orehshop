from django.db import models

class Information(models.Model):
	text = models.TextField("Информация")
	def __str__(self):
		return self.text

