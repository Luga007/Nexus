from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    image = models.ImageField(upload_to="")
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
