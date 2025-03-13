from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
