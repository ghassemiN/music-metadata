from django.db import models
# Create your models here.
class contributers(models.Model):
    contributer = models.CharField(max_length=255, unique=True)

class songs(models.Model):
    title = models.CharField(max_length=255)
    iswc = models.CharField(max_length=255, unique=True)

class song_contributer(models.Model):
    contributer = models.ForeignKey(contributers, on_delete=models.CASCADE)
    song = models.ForeignKey(songs, on_delete=models.CASCADE)

    class Meta:
    	unique_together = ('contributer', 'song',)