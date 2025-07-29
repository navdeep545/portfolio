from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	created_date = models.DateField(auto_now = True)
