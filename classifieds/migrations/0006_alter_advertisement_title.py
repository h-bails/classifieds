# Generated by Django 3.2.19 on 2023-06-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0005_advertisement_saved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
