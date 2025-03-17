from django.db import models
from user.models import Profile
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.IntegerField(default=0)
    description = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

class BlogImage(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="")
