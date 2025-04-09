from django.test import TestCase
from django.urls import reverse, resolve
from ..views import blog, post_list
class BlogUrlsTest(TestCase):
    def test_urls_blog(self):
        url = reverse('blog')
        self.assertEqual(resolve(url).func, blog)

    def test_urls_post_list(self):
        url = reverse('post', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, post_list)

