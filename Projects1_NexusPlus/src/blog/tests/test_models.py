from django.test import TestCase
from ..models import Blog, Comment

class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog.objects.create(title='Test', comment=85, like=0, views=0)
        self.assertEqual(blog.title, 'Test')
        self.assertEqual(blog.comment, 85)
        self.assertEqual(blog.like, 0)
        self.assertEqual(blog.views, 0)


    def test_create_comment(self):
        comment = Comment.objects.create(text='Hello world!')
        self.assertEqual(comment.text, 'Hello world!')
