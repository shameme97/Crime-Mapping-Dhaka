from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Area, CrimeIncident
from .forms import CreatePost

# Create your views here.


def index(response):
	return render(response, "main/base.html", {})

def home(response):
	return render(response, "main/home.html", {})

def areas(response):
	my_dict = {}
	total_areas = len(Area.objects.all())
	st = "<h1>Areas:</h1>"
	for i in range(1,total_areas+1):
		ls = Area.objects.get(id=i)
		# st += ls.area_name + " : " + str(ls.number_of_crimes) + "<br> </br>"
		# my_dict[i] = ls
		my_dict[ls.area_name] = ls.number_of_crimes

	# return HttpResponse("<p>%s</p>" %st)
	return render(response, "main/list.html", {'my_dict':my_dict})

def post(response):
	if response.method=="POST":
		form = CreatePost(response.POST)
		if form.is_valid():
			n = form.cleaned_data["nature"]
			d = form.cleaned_data["date"]
			t = form.cleaned_data["time"]
			a = form.cleaned_data["area_name"]
			l = form.cleaned_data["location"]
			rs = form.cleaned_data["report_status"]
			rid = form.cleaned_data["report_id"]
			desc = form.cleaned_data["description"]
			crime = CrimeIncident(nature_of_crime=n, date_of_crime=d, time_of_crime=t, area=a, location=l, report_status=rs, report_id=rid, description=desc)
			crime.save()
		return HttpResponseRedirect("/%i" %crime.id)
	else:
		form = CreatePost()
	return render(response, "main/post.html", {"form": form})