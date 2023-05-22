# Generated by Django 4.1 on 2023-05-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_journals_app', '0004_alter_bookdetailpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetailpost',
            name='slug',
            field=models.SlugField(blank=True, help_text='Re-type the name of your book', max_length=200, null=True, unique=True),
        ),
    ]
