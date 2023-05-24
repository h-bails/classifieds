from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import RandomCharField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ads")
    posted_on = models.DateField(auto_now=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    identifier = RandomCharField(length=8, editable=False, unique=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title

