from django.test import SimpleTestCase
from main.forms import CreatePost, PostComment
import datetime

class FormsTest(SimpleTestCase):
	
	def setUp(self):

		self.post1 = CreatePost(data={
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

		self.post2 = CreatePost(data={})

		self.comment1 = PostComment(data={
			'email' : 'abc@gmail.com',
			'comment' : '..........',
			'post_id' : 10
			})

		self.comment2 = PostComment(data={})


	def test_CreatePost_valid_data(self):
		self.assertTrue(self.post1.is_valid()) 

	def test_CreatePost_no_data(self):
		self.assertFalse(self.post2.is_valid())
		self.assertEquals(len(self.post2.errors), 8) # because 8 fields are mandatory

	def test_Comment_valid_data(self):
		self.assertTrue(self.comment1.is_valid())

	def test_Comment_no_data(self):
		self.assertFalse(self.comment2.is_valid())
		self.assertEquals(len(self.comment2.errors), 3) # because 3 fields are mandatory