# Generated by Django 3.2.7 on 2022-05-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        #('eclass', '0005_alter_class_options'),
        ('meeting', '0001_initial'),
        ('course', '0006_course_noticeobjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meetings',
            field=models.ManyToManyField(blank=True, related_name='meetings', to='meeting.Meeting'),
        ),
        #migrations.AlterField(
        #    model_name='course',
        #    name='classes',
        #    field=models.ManyToManyField(blank=True, related_name='classes', to='eclass.Class'),
        #),
    ]
