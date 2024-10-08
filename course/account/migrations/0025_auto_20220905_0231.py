# Generated by Django 3.2.7 on 2022-09-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20220526_1838'),
        ('account', '0024_auto_20220903_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='enrolled_courses',
            field=models.ManyToManyField(blank=True, related_name='enrolled_courses', to='course.Course'),
        ),
        migrations.AddField(
            model_name='account',
            name='enrollrequest_courses',
            field=models.ManyToManyField(blank=True, related_name='enroll_request_courses', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='account',
            name='dashboard_courses',
            field=models.ManyToManyField(blank=True, related_name='dashboard_courses', to='course.Course'),
        ),
    ]
