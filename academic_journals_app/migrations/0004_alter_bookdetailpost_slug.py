# Generated by Django 4.1 on 2023-05-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_journals_app', '0003_alter_bookdetailpost_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetailpost',
            name='slug',
            field=models.SlugField(blank=True, editable=False, help_text='Re-type the name of your book', max_length=200, null=True, unique=True),
        ),
    ]