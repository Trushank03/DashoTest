# Generated by Django 3.2.7 on 2022-11-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0028_alter_course_aboutthecourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abouttheCourse',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
