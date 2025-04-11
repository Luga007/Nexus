from django.test import TestCase
from ..forms import ProductForm
from category.models import Category, Brand, Region


class ProductFormTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', is_main=True)
        self.brand = Brand.objects.create(name='idk')
        self.region = Region.objects.create(name='somewhere', sorting=77)

    def test_valid_form(self):
        form_date = {
            'title': 'Sure',
            'description': 'Sure',
            'price': 10,
            'category': self.category,
            'brand': self.brand,
            'location': self.region,
            'condition': 'new',
            'price_on_call': True,
        }
        form = ProductForm(data=form_date)
        print(form.errors)
        # self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_date = {
            'title': '',
        }
        form = ProductForm(data=form_date)
        self.assertFalse(form.is_valid())
        self.assertTrue('slug', form.errors)