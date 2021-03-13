from django.db import models

# Create your models here.

class post(models.Model):
	name = models.CharField(max_length = 50)
	description = models.TextField()
	user_id = models.IntegerField(default = 1)
	#image = models.FileField(upload_to ='media',null='True',blank='True')

	def __str__(self):
		return self.name

