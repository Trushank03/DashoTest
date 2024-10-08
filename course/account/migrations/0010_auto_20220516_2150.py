# Generated by Django 3.2.7 on 2022-05-16 21:50

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='account',
            name='dobCert_doc',
            field=models.FileField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='account',
            name='govtId1_doc',
            field=models.FileField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='account',
            name='govtId2_doc',
            field=models.FileField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='account',
            name='institute',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='institute'),
        ),
        migrations.AddField(
            model_name='account',
            name='officeId_doc',
            field=models.FileField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='state'),
        ),
    ]
