# Generated by Django 3.2.7 on 2022-10-28 23:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0008_alter_chatcomment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='groupuserObjects',
            field=models.ManyToManyField(blank=True, related_name='groupuser_Objects', to=settings.AUTH_USER_MODEL),
        ),
    ]
