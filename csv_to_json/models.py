from django.db import models
# Create your models here.

class csvfile(models.Model):
	title = models.CharField(max_length=255)
	iswc = models.CharField(max_length=255, unique=True)
	contributer = models.CharField(max_length=255)