#   define the paths to our different webpages 
#	this file will represent the urls that goes into Views.py 

from django.urls import path
from . import views

urlpatterns = [ 
	path("", views.index, name="index"), 
	path("Home", views.home, name="home"),
	path("Home/AllPosts/", views.all_posts, name="all_posts"),
	path("Home/AllPosts/<str:filter1>", views.filter_all_posts, name="all_posts_filtering"),
	path("Areas", views.areas, name="areas"),
	path("post/", views.post, name="post"),
	path("incidents/<slug:area>/", views.show_posts, name="incidents"),
	path("incidents/<str:area>/<str:filter1>", views.filtering, name="filtering"),

]

