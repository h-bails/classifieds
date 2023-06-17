# Generated by Django 3.2.19 on 2023-06-17 15:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0007_auto_20230617_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_1'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_2'),
        ),
    ]