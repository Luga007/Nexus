from django.test import TestCase
from django.urls import resolve, reverse
from product.models import Product


class TestTemplates(TestCase):

    def setUp(self):
        self.product = Product.objects.create(title='Success', description='Test', price=100, condition=1, status=1)

    def test_product_templates(self):
        response = self.client.get(reverse('product'))
        self.assertContains(response, 'Success')
