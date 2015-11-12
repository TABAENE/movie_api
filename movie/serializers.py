
from rest_framework import serializers

from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
	
    owner = serializers.ReadOnlyField(source='owner.username')
	    
    class Meta:
        model = Movie
        fields = ('id', 'popularity', 'director', 'genre', 'imdb_score', 'name', 'owner')
