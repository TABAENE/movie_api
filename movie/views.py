from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
#~ from django.http import Http404
#from rest_framework.renderers import AdminRenderer

from movie.models import Movie
from movie.serializers import MovieSerializer
from movie.permissions import IsOwnerOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	#renderer_classes = (AdminRenderer,)
	#permission_classes = (IsOwnerOrReadOnly)
	
    #~ def list(self, request):
        #~ movies = Movie.objects.all()
        #~ serializer = MovieSerializer(movies, many=True)
        #~ return Response(serializer.data)
	
	def pre_save(self, obj):
		obj.owner = slef.request.user

class MovieList(APIView):
    """
    List all movie, or create a new movie.
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    #~ def get(self, request, format=None):
        #~ movies = Movie.objects.all()
        #~ serializer = MovieSerializer(movies, many=True)
        #~ context = {"records": serializer.data}
        #~ return Response(context)

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie.html'
	        
    def get(self, request):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        return Response({'profiles': queryset})  
		      
    #~ def get(self, request, format=None):
        #~ return render(request, 'index.html')

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class MovieDetail(APIView):
    """
    Retrieve, update or delete a movie instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#~ @api_view(('GET',))
#~ def api_root(request, format=None):
    #~ return Response({
        #~ 'users': reverse('user-list', request=request, format=format),
        #~ 'snippets': reverse('snippet-list', request=request, format=format)
    #~ })
    
def index(request):
	context = {}
	return render(request, 'index.html')
