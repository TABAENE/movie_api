from django import forms
from movie.models import Movie
from django.forms import ModelForm

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['popularity', 'director', 'genre', 'imdb_score', 'name', 'owner']
    

