from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from movie.views import index, MovieViewSet

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
#urlpatterns = router.urls
urlpatterns = [
	url(r'^movie/$', index), 	
	url(r'api/', include(router.urls)),
	#url(r'^index/(?P<pk>[0-9]+>)/$',MovieDetail.as_view()), 	
	#url(r'^$',api_root), 	
]
