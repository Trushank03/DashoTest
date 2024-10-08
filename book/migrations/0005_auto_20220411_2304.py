# Generated by Django 3.2.7 on 2022-04-11 23:04

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20220411_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='coverimage',
        ),
        migrations.RemoveField(
            model_name='imageuploadtest',
            name='coverImage',
        ),
        migrations.AddField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(blank=True, default=book.models.get_default_bookCoverImage, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='imageuploadtest',
            name='coverimage',
            field=models.FileField(blank=True, default=book.models.get_default_bookCoverImage, max_length=255, null=True, upload_to='images/'),
        ),
    ]
