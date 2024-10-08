# Generated by Django 3.2.7 on 2022-08-16 22:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_alter_chatgroup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='displayname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='groupuserObjects',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
