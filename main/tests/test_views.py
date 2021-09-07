from django.test import TestCase, Client
from django.urls import reverse
from main.models import CrimeIncident, Area, Comment
import datetime

class ViewsTest(TestCase):

	def setUp(self):
		self.client = Client()
		self.home_url = reverse('home')
		self.areas_url = reverse('areas')
		self.all_posts_url = reverse('all_posts')
		self.searchHome_url = reverse('searchHome', args=['Banani'])
		self.sort_areas_url = reverse('sort_areas', args=['Ascending'])
		self.search_in_areas_url = reverse('search_in_areas', args=['some_string'])
		self.post_url = reverse('post')
		self.comment_url = reverse('comment')
		self.show_posts_url = reverse('incidents', args=['Mohammadpur'])
		self.filtering_url = reverse('filtering', args=['Mohammadpur','Mugging'])
		self.filtering_url2 = reverse('filtering2', args=['Shyamoli','Mugging','Reported'])
		self.search_location_url = reverse('searchLocation', args=['Banani','location'])
		self.filter_by_date_url = reverse('filter_by_date', args=['Dhanmondi', 2018, 1, 1, 2021, 1, 1])
		self.filter_by_time_url = reverse('filter_by_time', args=['Banani', 5, 30, 7, 20])

		self.object1 = CrimeIncident.objects.create(
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

	def test_post_GET(self):
		response = self.client.get(self.post_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/post.html')

	def test_post_POST(self):
		response = self.client.post(self.post_url, {
			'email' : 'abc@gmail.com',
			'date' : datetime.date(2010, 1, 1),
			'time' : datetime.time(10, 33, 00),
			'nature' : 'Assault',
			'area_name' : 'Banani',
			'location' : 'road-2',
			'report_status' : 'Reported',
			'report_id' : '827526',
			'description' : '........'
			})

		self.assertEquals(response.status_code, 302)
		url = "http://127.0.0.1:8000/Areas/incidents/"+"Banani"
		self.assertRedirects(response, url, fetch_redirect_response=False)

	def test_post_POST_Report_status_as_Not_Reported(self):
		response = self.client.post(self.post_url, {
			'email' : 'abc@gmail.com',
			'date' : datetime.date(2010, 1, 1),
			'time' : datetime.time(10, 33, 00),
			'nature' : 'Assault',
			'area_name' : 'Shyamoli',
			'location' : 'road-2',
			'report_status' : 'Not Reported',
			# 'report_id' : '827526',
			'description' : '........'
			})

		self.assertEquals(response.status_code, 302)
		url = "http://127.0.0.1:8000/Areas/incidents/"+"Shyamoli"
		self.assertRedirects(response, url, fetch_redirect_response=False)

	def test_comment_GET(self):
		response = self.client.get(self.comment_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/comment.html')

	def test_comment_POST(self):
		response = self.client.post(self.comment_url, {
			'email' : 'abc@gmail.com',
			'comment' : '..........',
			'post_id' : 2
			})
		
		self.assertEquals(response.status_code, 302)
		url = "http://127.0.0.1:8000/Areas/incidents/"+"Dhanmondi"
		self.assertRedirects(response, url, fetch_redirect_response=False)

	def test_comment_POST_postID_does_not_exist(self):
		response = self.client.post(self.comment_url, {
			'email' : 'abc@gmail.com',
			'comment' : '..........',
			'post_id' : 10
			})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/comment.html')

	def test_home(self):
		response = self.client.get(self.home_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/home.html')

	def test_areas(self):
		response = self.client.get(self.areas_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/list.html')

	def test_all_posts(self):
		response = self.client.get(self.all_posts_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/home.html')

	def test_searchHome(self):
		response = self.client.get(self.searchHome_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/home.html')

	def test_sort_areas(self):
		response = self.client.get(self.sort_areas_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/list.html')

	def test_search_in_areas(self):
		response = self.client.get(self.search_in_areas_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/list.html')
	
	def test_show_posts(self):
		response = self.client.get(self.show_posts_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

	def test_filtering(self):
		response = self.client.get(self.filtering_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

	def test_filtering_with_2_filters(self):
		response = self.client.get(self.filtering_url2)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

	def test_search_location(self):
		response = self.client.get(self.search_location_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

	def test_filter_by_date(self):
		response = self.client.get(self.filter_by_date_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

	def test_filter_by_time(self):
		response = self.client.get(self.filter_by_time_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/incidents.html')

