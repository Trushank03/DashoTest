# Generated by Django 3.2.7 on 2024-06-20 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eclass', '0005_class_participants'),
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='class_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eclass.class'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='no_of_students_enrolled',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assignment',
            name='no_of_students_submitted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('reviewed', 'Reviewed')], default='open', max_length=10),
        ),
        migrations.AddField(
            model_name='assignment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='assignmentattachment',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='assignment.assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentattachment',
            name='afile',
            field=models.FileField(blank=True, max_length=1055, null=True, upload_to='documents/'),
        ),
    ]
