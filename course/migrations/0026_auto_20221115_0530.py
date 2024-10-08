# Generated by Django 3.2.7 on 2022-11-15 05:30

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_alter_course_courseshortname'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('fileaddress', models.FileField(blank=True, max_length=1055, null=True, upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('creationTime', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'ordering': ('creationDate',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='coursefiles',
            field=models.ManyToManyField(blank=True, related_name='course_file_objects', to='course.FileObject'),
        ),
    ]
