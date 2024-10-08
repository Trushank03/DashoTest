# Generated by Django 3.2.7 on 2022-04-10 02:27

import book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapterNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterno', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookSectionNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionno', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('caption', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('caption', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(blank=True, default=book.models.get_default_bookCoverImage, max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentences', models.ManyToManyField(blank=True, to='book.Sentence')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('questions', models.ManyToManyField(blank=True, to='book.Question')),
            ],
        ),
        migrations.CreateModel(
            name='BookSubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sectionid', models.IntegerField(blank=True, null=True)),
                ('paragraphs', models.ManyToManyField(blank=True, to='book.Paragraph')),
            ],
        ),
        migrations.CreateModel(
            name='BookSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('chapterid', models.IntegerField(blank=True, null=True)),
                ('figures', models.ManyToManyField(blank=True, to='book.Figure')),
                ('paragraphs', models.ManyToManyField(blank=True, to='book.Paragraph')),
                ('sectionnum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.booksectionnumber')),
                ('subsections', models.ManyToManyField(blank=True, to='book.BookSubSection')),
                ('tables', models.ManyToManyField(blank=True, to='book.Table')),
            ],
        ),
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bookid', models.IntegerField(blank=True, null=True)),
                ('chapternum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.bookchapternumber')),
                ('exercises', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.exercise')),
                ('sections', models.ManyToManyField(blank=True, to='book.BookSection')),
            ],
            options={
                'ordering': ('chapternum',),
            },
        ),
        migrations.AddField(
            model_name='book',
            name='chapters',
            field=models.ManyToManyField(blank=True, to='book.BookChapter'),
        ),
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.content'),
        ),
    ]
