from django.test import TestCase
from django.urls import reverse, resolve
from ..views import login_view, register

class TestUrls(TestCase):
    def test_login_view(self):
        url = reverse('login_view')
        self.assertEqual(resolve(url).func, login_view)

    def test_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)