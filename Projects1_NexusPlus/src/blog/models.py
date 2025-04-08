from django.db import models
from user.models import Profile, User
from category.models import Category


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comments = models.IntegerField(default=0)
    description = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True, editable=False, null=False)

    def __str__(self):
        return '%s %s' % (self.blog.id, self.text)


class BlogImage(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="")
