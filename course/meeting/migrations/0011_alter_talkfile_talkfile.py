# Generated by Django 3.2.7 on 2022-08-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0010_auto_20220802_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkfile',
            name='talkfile',
            field=models.FileField(blank=True, max_length=5000, null=True, upload_to='images/'),
        ),
    ]
