from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from ..models import Profile

class ViewsTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(firstname='John', last_name='Smith', phone_number='555-555-5555', bio='Sure')


    def test_log_in_view(self):
        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code, 200)

    def test_log_in_list_templates_used(self):
        response = self.client.get(reverse('login_view'))
        self.assertTemplateUsed(response, 'login.html')

    # def test_blog_list_view_context(self):
    #     response = self.client.get(reverse('login_view'))
    #     self.assertIn(self.profile, response.context['login_view'])