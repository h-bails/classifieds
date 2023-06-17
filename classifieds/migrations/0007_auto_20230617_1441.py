# Generated by Django 3.2.19 on 2023-06-17 14:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0006_alter_advertisement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]