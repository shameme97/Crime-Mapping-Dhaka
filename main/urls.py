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
	path("Areas/<str:sort>", views.sort_areas, name="sort_areas"),
	path("post/", views.post, name="post"),
	path("comment/", views.comment, name="comment"),
	path("incidents/<slug:area>/", views.show_posts, name="incidents"),
	path("incidents/<str:area>/<str:filter1>/", views.filtering, name="filtering"),
	path("incidents/<str:area>/<str:filter1>/<str:filter2>/", views.filtering, name="filtering"),
	path("incidents/<str:area>/<str:location>", views.search_location, name="searchLocation"),
	path("incidents/<str:area>/<int:y1>/<int:m1>/<int:d1>/<int:y2>/<int:m2>/<int:d2>", views.filter_by_date, name="filter_by_date"),
	path("incidents/<str:area>/time/<int:h1>:<int:m1>/<int:h2>:<int:m2>", views.filter_by_time, name="filter_by_time"),

]

