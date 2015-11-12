from django.db import models

# Create your models here.

class Movie(models.Model):
	
	#owner = models.ForeignKey('auth.User', related_name='movie')
	name = models.CharField(max_length=100)
	imdb_score = models.SmallIntegerField()
	director = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	popularity = models.IntegerField()
