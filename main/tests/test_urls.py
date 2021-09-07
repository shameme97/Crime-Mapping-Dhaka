from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import (index, home, sort_areas, all_posts, searchHome, areas, search_in_areas, 
	post, comment, show_posts, filtering, search_location, filter_by_date, filter_by_time)

class UrlsTest(SimpleTestCase):

	def test_index_url(self):
		url = reverse('index')
		self.assertEquals(resolve(url).func, home)

	def test_home_url(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_all_posts_url(self):
		url = reverse('all_posts')
		self.assertEquals(resolve(url).func, all_posts)

	def test_searchHome_url(self):
		url = reverse('searchHome', args=['Banani'])
		self.assertEquals(resolve(url).func, searchHome)

	def test_areas_url(self):
		url = reverse('areas')
		self.assertEquals(resolve(url).func, areas)

	def test_sort_areas_url(self):
		url = reverse('sort_areas', args=['Ascending'])
		self.assertEquals(resolve(url).func, sort_areas)

	def test_search_in_areas_url(self):
		url = reverse('search_in_areas', args=['some_string'])
		self.assertEquals(resolve(url).func, search_in_areas)

	def test_post_url(self):
		url = reverse('post')
		self.assertEquals(resolve(url).func, post)

	def test_comment_url(self):
		url = reverse('comment')
		self.assertEquals(resolve(url).func, comment)

	def test_incidents_url(self):
		url = reverse('incidents', args=['area_name'])
		self.assertEquals(resolve(url).func, show_posts)

	def test_filtering_url(self):
		url = reverse('filtering', args=['area_name','filter_1'])
		self.assertEquals(resolve(url).func, filtering)

	def test_filtering2_url(self):
		url = reverse('filtering2', args=['Shyamoli','filter_1','filter_2'])
		self.assertEquals(resolve(url).func, filtering)

	def test_searchLocation_url(self):
		url = reverse('searchLocation', args=['Banani','location'])
		self.assertEquals(resolve(url).func, search_location)

	def test_filter_by_date_url(self):
		url = reverse('filter_by_date', args=['Dhanmondi', 2018, 1, 1, 2021, 1, 1])
		# print(resolve(url))
		self.assertEquals(resolve(url).func, filter_by_date)

	def test_filter_by_time_url(self):
		url = reverse('filter_by_time', args=['Banani', 5, 30, 7, 20])
		# print(resolve(url))
		self.assertEquals(resolve(url).func, filter_by_time)
