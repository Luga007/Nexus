from django.test import TestCase
from django.urls import resolve, reverse
from ..models import Blog

class BlogTemplateTest(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(title='Test Blog', comment=10, like=20, description='xd', views=10)


    def test_blog_templates_test(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response, 'Test Blog')