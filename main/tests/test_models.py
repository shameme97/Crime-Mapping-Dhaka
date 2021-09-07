from django.test import TestCase
from main.models import CrimeIncident, Area, Comment
import datetime


class ModelsTest(TestCase):

	def setUp(self):

		self.incident1 = CrimeIncident.objects.create(
			id = 2,
			email = 'abc@gmail.com',
			username = 'abcd1234',
			area_name = 'Dhanmondi',
			nature_of_crime = 'Mugging',
			report_status = 'Reported',
			report_id = '73822',
			location = 'road-13',
			date_of_crime = datetime.date(2020, 5, 10),
			time_of_crime = datetime.time(11, 30, 00),
			timestamp = datetime.datetime.now(),
			description = '.........'
			)

		self.area1 = Area.objects.create(
			id = 1,
			name = 'Mohammadpur',
			number_of_crimes = 10
			)

		self.comment1 = Comment.objects.create(
			id = 1,
			email = 'abc@gmail.com',
			username = 'abc123',
			comment = 'bla bla bla',
			post_id = 2
			)


	def test_CrimeIncident__str__(self):
		self.assertEquals(str(self.incident1), "Mugging committed in Dhanmondi")

	def test_Area__str__(self):
		self.assertEquals(str(self.area1), "Mohammadpur : 10")

	def test_Comment__str__(self):
		self.assertEquals(str(self.comment1), "abc123 commented on Post: 2")

