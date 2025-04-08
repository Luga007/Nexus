from django.test import TestCase
from category.models import Category, Brand, Region


class CategoryTestCase(TestCase):
    def test_create_category(self):
        name = 'Phone'
        is_main = True
        slug = 'phone'
        category = Category.objects.create(name=name, is_main=is_main, slug=slug)
        self.assertEqual(category.name, 'Phone')
        self.assertEqual(category.slug, 'phone')
        self.assertTrue(category.is_main)
        self.assertIsNone(category.parent)

    def test_create_category_with_parent(self):
        parent = Category.objects.create(name='Elektronik', slug='Elektronik')
        sub = Category.objects.create(name='Phone', slug='phone', parent=parent)
        self.assertEqual(sub.parent, parent)


class RegionTestCase(TestCase):
    def test_create_region(self):
        region = Region.objects.create(name='Navoi', sorting='7')
        self.assertEqual(region.name, 'Navoi')
        self.assertEqual(region.sorting, '7')


class BrandTestCase(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name='Samsung')
        self.assertEqual(brand.name, 'Samsung')
