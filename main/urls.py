#   define the paths to our different webpages 
#	this file will represent the urls that goes into Views.py 

from django.urls import path
from . import views

urlpatterns = [ 
	path("", views.index, name="index"), 
	path("Home", views.home, name="home"),
	path("Areas", views.areas, name="areas"),
	path("post/", views.post, name="post"),
	path("incidents/", views.show_posts, name="incidents")
]

