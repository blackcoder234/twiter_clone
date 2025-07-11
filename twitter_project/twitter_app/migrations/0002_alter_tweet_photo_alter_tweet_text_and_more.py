# Generated by Django 5.2.1 on 2025-06-07 03:17

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(max_length=280),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
