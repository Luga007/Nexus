from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    firstname = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.last_name)
