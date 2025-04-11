from django.test import TestCase
from product.models import Product, ProductView, ProductImage
from category.models import Region


class ProductTestCreate(TestCase):
    def test_create_product(self):
        # location = Region.objects.create(name='Tashkent', sorting=1)
        product = Product.objects.create(title='Test', description='Test', price=100, condition=1, status=1)
        self.assertEqual(product.title, 'Test')
        self.assertEqual(product.description, 'Test')
        self.assertEqual(product.price, 100)
        self.assertEqual(product.condition, 1)
        self.assertEqual(product.status, 1)
        # self.assertEqual(product.location, location)

    def product_view_create(self):
        views = ProductView.objects.create(view_count=20)
        self.assertEqual(views.view_count, 20)


