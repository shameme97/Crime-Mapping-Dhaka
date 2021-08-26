from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Area, CrimeIncident, Comment
from .forms import CreatePost, PostComment
import random
import string 
import datetime
import operator

# Create your views here.


def index(response):
	return render(response, "main/base.html", {})

def home(response):
	msg = "Home/AllPosts"
	return render(response, "main/home.html", {'Msg':msg})

def all_posts(request):
	my_dict = {}
	count = 0
	if request.method=="GET" or True:
		msg = ""
		for i in list(CrimeIncident.objects.all()):
			count += 1
			incident = {
						'Post ID' : i.id,
						'Username' : i.username,
						'Posted on' : i.timestamp,
						'Nature of crime' : i.nature_of_crime,
						'Location' : i.location+", "+i.area_name,
						'Date' : i.date_of_crime,
						'Time' : i.time_of_crime,
						'Report Status' : i.report_status,
					}
			if i.report_status=="Reported":
				incident.update({'Report ID' : "#"+i.report_id})
			incident.update({'Description' : i.description})
			my_dict[i] = incident
		no_of_posts = {'Number of posts:':count}
		return render(request, "main/home.html", {'my_dict':my_dict, 'Msg':msg, 'no_of_posts':no_of_posts})

def searchHome(request, area):
	my_dict={}
	count=0
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if i.area_name.lower().startswith(area.lower()):
				incident = {
					'Post ID' : i.id,
					'Username' : i.username,
					'Posted on' : i.timestamp,
					'Nature of crime' : i.nature_of_crime,
					'Location' : i.location+", "+i.area_name,
					'Date' : i.date_of_crime,
					'Time' : i.time_of_crime,
					'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})
				incident.update({'Description' : i.description})
				my_dict[i] = incident
				count += 1

		no_of_posts = {'Number of posts:':count}
	return render(request, "main/home.html", {'my_dict':my_dict, 'no_of_posts':no_of_posts})

def areas(response):
	my_dict = {}
	for obj in list(Area.objects.all()):
		my_dict[obj.name] = obj.number_of_crimes
	return render(response, "main/list.html", {'my_dict':my_dict})

def sort_areas(request, sort):
	my_dict = {}
	if request.method=="GET":
		for area in list(Area.objects.all()):
			my_dict[area.name] = area.number_of_crimes
		if sort == 'Ascending':
			my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
		elif sort == 'Descending':
			my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
	return render(request, "main/list.html", {'my_dict':my_dict})


def search_in_areas(request, area):
	my_dict = {}
	if request.method=="GET":
		for i in list(Area.objects.all()):
			if i.name.lower().startswith(area.lower()):
				my_dict[i.name] = i.number_of_crimes	
	return render(request, "main/list.html", {'my_dict':my_dict})

	
def post(response):
	if response.method=="POST":
		form = CreatePost(response.POST)
		error=""	
		if form.is_valid():
			e = form.cleaned_data["email"]
			n = form.cleaned_data["nature"]
			if n=="Choose":
				error = "Please choose nature of crime!"	
			d = form.cleaned_data["date"]
			t = form.cleaned_data["time"]
			a = form.cleaned_data["area_name"]
			a = a[0].upper() + a[1:].lower()
			l = form.cleaned_data["location"]
			rs = form.cleaned_data["report_status"]
			rid = form.cleaned_data["report_id"]
			if rs=="Reported" and rid=="":
				error = "Please enter report ID!"
			desc = form.cleaned_data["description"]
			random_name = ''
			for user in CrimeIncident.objects.filter(email=e):
				random_name = user.username
			if random_name=='':
				random_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
			if error!="":
				return render(response, "main/post.html", {"form": form,"Error":error})
			crime = CrimeIncident(nature_of_crime=n, date_of_crime=d, time_of_crime=t, area_name=a, location=l, report_status=rs, report_id=rid, description=desc, email=e, username=random_name, timestamp=datetime.datetime.now())
			crime.save()

			if Area.objects.filter(name=a).exists():
				ls = Area.objects.get(name=a)
				ls.number_of_crimes+=1
				ls.save()
			else:
				ls = Area(name=a,number_of_crimes=1)
				ls.save()
		
			return HttpResponseRedirect("http://127.0.0.1:8000/Areas/incidents/"+a)
	else:
		form = CreatePost()
	return render(response, "main/post.html", {"form": form})

def comment(response):
	if response.method=="POST":
		form = PostComment(response.POST)	
		if form.is_valid():
			e = form.cleaned_data["email"]
			p = form.cleaned_data["post_id"]
			c = form.cleaned_data["comment"]
			user_name = ''
			for incident in list(CrimeIncident.objects.all()):
				if e == incident.email:
					user_name = incident.username
			for com in list(Comment.objects.all()):
				if e == com.email:
					user_name = com.username
			if user_name=='':	
				user_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
			
			if len(CrimeIncident.objects.filter(id=p))==0:
				error = "Post ID does not exist!"
				return render(response, "main/comment.html", {"form": form, "Error": error})
			else:
				page = CrimeIncident.objects.get(id=p).area_name
			com = Comment(email=e, username=user_name, comment=c, post_id=p)
			com.save()
			
			return HttpResponseRedirect("http://127.0.0.1:8000/Areas/incidents/"+page)
	else:
		form = PostComment()
	return render(response, "main/comment.html", {"form": form})

def show_posts(request, area):
	posts = {}
	count=0
	comments ={}
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if i.area_name.lower() == area.lower():
				count += 1
				incident = {
					'Post ID' : i.id,
					'Username' : i.username,
					'Posted on' : i.timestamp,
					'Nature of crime' : i.nature_of_crime,
					'Location' : i.location+", "+i.area_name,
					'Date' : i.date_of_crime,
					'Time' : i.time_of_crime,
					'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})	
				incident.update({'Description' : i.description})

				comment = {}
				for j in Comment.objects.filter(post_id=i.id):
					comment.update( {j.comment: 'User '+j.username+' commented: '})
					comments[i] = comment

				posts[i] = incident
		no_of_posts = {'Number of posts:':count}
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area, 'no_of_posts':no_of_posts, 'comments':comments})


def filtering(request, area, filter1, filter2=""):
	posts = {}
	comments={}
	count=0
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if (i.nature_of_crime==filter1 or i.report_status==filter1) and i.area_name.lower()==area.lower():
				incident = {
					'Post ID' : i.id,
					'Username' : i.username,
					'Posted on' : i.timestamp,
					'Nature of crime' : i.nature_of_crime,
					'Location' : i.location+", "+i.area_name,
					'Date' : i.date_of_crime,
					'Time' : i.time_of_crime,
					'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})
				incident.update({'Description' : i.description})

				if filter2=="":
					posts[i] = incident
					count+=1
					comment = {}
					for j in Comment.objects.filter(post_id=i.id):
						comment.update( {j.comment: 'User '+j.username+' commented: '})
						comments[i] = comment

				elif (i.nature_of_crime==filter2 or i.report_status==filter2):
					incident = {
						'Post ID' : i.id,
						'Username' : i.username,
						'Posted on' : i.timestamp,
						'Nature of crime' : i.nature_of_crime,
						'Location' : i.location+", "+i.area_name,
						'Date' : i.date_of_crime,
						'Time' : i.time_of_crime,
						'Report Status' : i.report_status,
					}
					if i.report_status=="Reported":
						incident.update({'Report ID' : "#"+i.report_id})
					incident.update({'Description' : i.description})
					count+=1
					posts[i] = incident

					comment = {}
					for j in Comment.objects.filter(post_id=i.id):
						comment.update( {j.comment: 'User '+j.username+' commented: '})
						comments[i] = comment

			no_of_posts = {'Number of posts:':count}
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area, 'no_of_posts':no_of_posts, 'comments':comments})


def search_location(request, area, location):
	posts={}
	comments={}
	count=0
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if location.lower() in i.location.lower() and i.area_name.lower() ==area.lower() :
				incident = {
					'Post ID' : i.id,
					'Username' : i.username,
					'Posted on' : i.timestamp,
					'Nature of crime' : i.nature_of_crime,
					'Location' : i.location+", "+i.area_name,
					'Date' : i.date_of_crime,
					'Time' : i.time_of_crime,
					'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})
				incident.update({'Description' : i.description})
				posts[i] = incident
				count += 1

				comment = {}
				for j in Comment.objects.filter(post_id=i.id):
					comment.update( {j.comment: 'User '+j.username+' commented: '})
					comments[i] = comment

		no_of_posts = {'Number of posts:':count}
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area, 'no_of_posts':no_of_posts, 'comments':comments})


def filter_by_date(request, area, y1, m1, d1, y2, m2, d2):
	posts={}
	comments={}
	count=0
	from_date = datetime.date(y1,m1,d1)
	to_date = datetime.date(y2,m2,d2)
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if i.area_name.lower()==area.lower() and from_date<=i.date_of_crime<=to_date:
				incident = {
						'Post ID' : i.id,
						'Username' : i.username,
						'Posted on' : i.timestamp,
						'Nature of crime' : i.nature_of_crime,
						'Location' : i.location+", "+i.area_name,
						'Date' : i.date_of_crime,
						'Time' : i.time_of_crime,
						'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})
				incident.update({'Description' : i.description})
				posts[i] = incident
				count +=1 

				comment = {}
				for j in Comment.objects.filter(post_id=i.id):
					comment.update( {j.comment: 'User '+j.username+' commented: '})
					comments[i] = comment

		no_of_posts = {'Number of posts:':count}
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area, 'no_of_posts':no_of_posts, 'comments':comments})


def filter_by_time(request, area, h1, m1, h2, m2):
	posts={}
	comments={}
	count=0
	from_time = datetime.time(h1,m1)
	to_time = datetime.time(h2,m2)
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if i.area_name.lower()==area.lower() and from_time<=i.time_of_crime<=to_time:
				incident = {
						'Post ID' : i.id,
						'Username' : i.username,
						'Posted on' : i.timestamp,
						'Nature of crime' : i.nature_of_crime,
						'Location' : i.location+", "+i.area_name,
						'Date' : i.date_of_crime,
						'Time' : i.time_of_crime,
						'Report Status' : i.report_status,
				}
				if i.report_status=="Reported":
					incident.update({'Report ID' : "#"+i.report_id})
				incident.update({'Description' : i.description})
				posts[i] = incident
				count += 1

				comment = {}
				for j in Comment.objects.filter(post_id=i.id):
					comment.update( {j.comment: 'User '+j.username+' commented: '})
					comments[i] = comment

		no_of_posts = {'Number of posts:':count}
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area, 'no_of_posts':no_of_posts,'comments':comments})


