from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True) 									# blank=True means optional


# anytime some changes applied to models it needs to be applied to the database. thats called 'migration'