# Generated by Django 4.1 on 2023-05-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_journals_app', '0002_bookdetailpost_delete_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetailpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='academic_journals_app.user'),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Choose the ctegory your book fall in.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='academic_journals_app.category'),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='description',
            field=models.CharField(help_text='A short descriptionof your book', max_length=500),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='keywords',
            field=models.CharField(blank=True, help_text='Choose keywords to locate your book easier', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='slug',
            field=models.SlugField(blank=True, help_text='Re-type the name of your book', max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bookdetailpost',
            name='title',
            field=models.CharField(help_text='The nme of your book', max_length=200, unique=True),
        ),
    ]
