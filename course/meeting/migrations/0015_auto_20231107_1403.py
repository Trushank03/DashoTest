# Generated by Django 3.2.7 on 2023-11-07 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0014_alter_meeting_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ('datetime',)},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='meetingdate',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='meetingtime',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='roomNo',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='topics',
        ),
    ]
