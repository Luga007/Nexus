from django.test import TestCase
from product.models import Product, ProductView, ProductImage


class ProductTestCreate(TestCase):
    def test_create_product(self):
        product = Product.objects.create(title='Test', description='Test', price=100, condition=1, status=1)
        self.assertEqual(product.title, 'Test')
        self.assertEqual(product.description, 'Test')
        self.assertEqual(product.price, 100)
        self.assertEqual(product.condition, 1)
        self.assertEqual(product.status, 1)

    def product_view_create(self):
        views = ProductView.objects.create(view_count=20)
        self.assertEqual(views.view_count, 20)


