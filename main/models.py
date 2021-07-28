from django.db import models

# Create your models here.

class CrimeIncident(models.Model):
	# incident = models.ForeignKey(Area, on_delete=models.CASCADE)
	email = models.CharField(max_length=50)
	username = models.CharField(max_length=20)
	area_name = models.CharField(max_length=150)
	nature_of_crime = models.CharField(max_length=50)
	report_status = models.BooleanField()
	report_id = models.IntegerField()
	location = models.CharField(max_length=100)
	date_of_crime = models.DateField()
	time_of_crime = models.TimeField()
	timestamp = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.nature_of_crime+" committed in "+ self.area_name 

class Area(models.Model):
	# incident = models.ForeignKey(CrimeIncident, on_delete=models.CASCADE)
	name = models.CharField(max_length=150)
	number_of_crimes = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.name)+" : "+str(self.number_of_crimes)