# Generated by Django 3.2.7 on 2023-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
        ('account', '0038_auto_20230909_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='myinstitutes',
            field=models.ManyToManyField(blank=True, related_name='my_institutes', to='institute.Institute'),
        ),
    ]
