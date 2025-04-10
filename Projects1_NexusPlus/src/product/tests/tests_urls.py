from django.test import TestCase
from django.urls import reverse, resolve
from product.models import Product, ProductView
from product.views import products, details, product_add, dashboard

class TestUrls(TestCase):
    def test_urls(self):
        url1 = reverse('product')
        url2 = reverse('details',  kwargs={'pk': 1})
        url3 = reverse('product-add')
        url4 = reverse('dashboard')
        self.assertEqual(resolve(url1).func, products)
        self.assertEqual(resolve(url2).func, details)
        self.assertEqual(resolve(url3).func, product_add)
        self.assertEqual(resolve(url4).func, dashboard)
