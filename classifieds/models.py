from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import RandomCharField
from cloudinary.models import CloudinaryField


# Model for the different advertisement categories
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Model for the advertisements
class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ads")
    posted_on = models.DateField(auto_now=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    identifier = RandomCharField(length=8, editable=False, unique=True)
    saved_by = models.ManyToManyField(
        User, related_name="saved_ads", blank=True)
    image_1 = CloudinaryField('image_1', blank=True, null=True)
    image_2 = CloudinaryField('image_2', blank=True, null=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title
