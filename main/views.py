from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Area, CrimeIncident
from .forms import CreatePost
import random
import string 
import datetime

# Create your views here.


def index(response):
	# my_dict = {
	# 	'ID': slug
	# }
	return render(response, "main/base.html", {})

def home(response):
	return render(response, "main/home.html", {})

def areas(response):
	my_dict = {}
	for obj in list(Area.objects.all()):
		my_dict[obj.name] = obj.number_of_crimes
	return render(response, "main/list.html", {'my_dict':my_dict})

def show_posts(request, area):
	posts = {}
	if request.method=="GET":
		for i in list(CrimeIncident.objects.all()):
			if i.area_name == area:
				# incident = ["Post ID : "+ str(i.id)]
				# incident += ["Username : "+i.username, "Posted on : "+str(i.timestamp)] 
				# incident +=	["Nature of crime : "+i.nature_of_crime, "Location : "+i.location]
				# incident += ["Date : "+str(i.date_of_crime), "Time : "+str(i.time_of_crime)]
				# incident += ["Report Status : "+str(i.report_status), "Report ID : "+str(i.report_id)]
				# incident += ["Description : "+i.description]

				incident = {
					'Post ID' : i.id,
					'Username' : i.username,
					'Posted on' : i.timestamp,
					'Nature of crime' : i.nature_of_crime,
					'Location' : i.location,
					'Date' : i.date_of_crime,
					'Time' : i.time_of_crime,
					'Report Status' : i.report_status,
					'Report ID' : i.report_id,
					'Description' : i.description

				}
				posts[i] = incident
	return render(request, "main/incidents.html", {'Posts':posts, 'Area':area})

def post(response):
	if response.method=="POST":
		form = CreatePost(response.POST)
		if form.is_valid():
			e = form.cleaned_data["email"]
			n = form.cleaned_data["nature"]
			d = form.cleaned_data["date"]
			t = form.cleaned_data["time"]
			a = form.cleaned_data["area_name"]
			l = form.cleaned_data["location"]
			rs = form.cleaned_data["report_status"]
			rid = form.cleaned_data["report_id"]
			desc = form.cleaned_data["description"]
			random_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
			crime = CrimeIncident(nature_of_crime=n, date_of_crime=d, time_of_crime=t, area_name=a, location=l, report_status=rs, report_id=rid, description=desc, email=e, username=random_name, timestamp=datetime.datetime.now())
			crime.save()

			if Area.objects.filter(name=a).exists():
				ls = Area.objects.get(name=a)
				ls.number_of_crimes+=1
				ls.save()
			else:
				ls = Area(name=a,number_of_crimes=1)
				ls.save()

		
		return HttpResponseRedirect("/Areas")
		# return render(response, "main/list.html", {})
	else:
		form = CreatePost()
	return render(response, "main/post.html", {"form": form})