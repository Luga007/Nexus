from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from category.models import Category
from category.views import category_views

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category', slug='test-category', is_main=True
        )

    # def test_category_list_view_status_code(self):
    #     url = reverse('category')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)


    # def test_category_view_status(self):
    #     response = self.client.get(reverse('category'))
    #     self.assertTemplateUsed(response, 'category/product.html')