# Generated by Django 4.1 on 2023-05-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_journals_app', '0007_alter_bookdetailpost_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetailpost',
            name='book',
            field=models.FileField(help_text='Upload your book here', null=True, upload_to='books/'),
        ),
    ]