# Generated by Django 3.2.7 on 2022-05-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20220516_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dobCert_doc',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='govtId1_doc',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='govtId2_doc',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='officeId_doc',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]
