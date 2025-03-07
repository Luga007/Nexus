from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    image = models.ImageField(upload_to="")
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    sorting = models.SmallIntegerField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.name
