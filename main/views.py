from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Area, CrimeIncident
from .forms import CreatePost
import random
import string 
import datetime

# Create your views here.


def index(response):
	return render(response, "main/base.html", {})

def home(response):
	return render(response, "main/home.html", {})

def areas(response):
	my_dict = {}
	i=0
	for obj in list(Area.objects.all()):
		my_dict[i] = obj
		i += 1
	return render(response, "main/list.html", {'my_dict':my_dict})

def show_posts(response):
	return render(response, "main/incidents.html", {})

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

		
		# return HttpResponseRedirect("/%i" %crime.id)
		return render(response, "main/home.html", {})
	else:
		form = CreatePost()
	return render(response, "main/post.html", {"form": form})