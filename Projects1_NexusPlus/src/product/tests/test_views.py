from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from product.models import Product, ProductView

class TestProduct(TestCase):
    def setUp(self):
        self.product = Product.objects.create(title='Test', description='Test', price=100, condition=1, status=1)

    def test_product_view_status(self):
        response = self.client.get(reverse('product'))
        self.assertEqual(response.status_code, 200)


    def test_product_templates_used(self):
        response1 = self.client.get(reverse('product'))
        self.assertTemplateUsed(response1, 'product.html')
        # response2 = self.client.get(reverse('details', kwargs={'pk': 1}))
        # self.assertTemplateUsed(response2, 'detail.html')
        response3 = self.client.get(reverse('product-add'))
        self.assertTemplateUsed(response3, 'post-ads.html')
        response4 = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response4, 'dashboard.html')