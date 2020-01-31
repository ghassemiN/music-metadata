from django.db import models
# Create your models here.
class myfile(models.Model):
    title = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    iswc = models.CharField(max_length=255)
