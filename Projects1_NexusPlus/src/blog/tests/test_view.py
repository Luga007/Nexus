from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from ..models import Blog


class CategoryTests(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(title='Blog', comments=7, description='sss', like=10, views=200)

    def test_blog_list_view_status_code(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_templates_used(self):
        response = self.client.get(reverse('blog'))
        self.assertTemplateUsed(response, 'blog.html')

    def test_blog_list_view_context(self):
        response = self.client.get(reverse('blog'))
        self.assertIn(self.blog, response.context['blogs'])