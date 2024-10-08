# Generated by Django 3.2.7 on 2023-01-10 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_alter_institute_instlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefullLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('creationDateTime',),
            },
        ),
        migrations.AddField(
            model_name='account',
            name='usefull_links',
            field=models.ManyToManyField(blank=True, to='account.UsefullLink'),
        ),
    ]
