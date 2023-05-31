# Generated by Django 4.1 on 2023-05-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_journals_app', '0016_alter_bookdetailpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_author', models.CharField(blank=True, help_text='Seo author name', max_length=200, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='Seo description', max_length=200, null=True)),
                ('meta_keywords', models.TextField(blank=True, help_text='Seo keywords', null=True)),
                ('title', models.CharField(blank=True, default='My site', help_text='Name of your site', max_length=200, null=True)),
                ('favicon', models.ImageField(blank=True, help_text='image that appears on your url', null=True, upload_to='')),
                ('logo', models.ImageField(blank=True, help_text='Logo that appears on your site', null=True, upload_to='')),
                ('site_description', models.CharField(blank=True, help_text='A logo alternative in written form', max_length=300, null=True)),
                ('footer_title', models.CharField(blank=True, help_text='Your footer title', max_length=300, null=True)),
                ('footer_description', models.CharField(blank=True, help_text='Your footer description', max_length=300, null=True)),
                ('facebook', models.URLField(blank=True, help_text='Facebook url', null=True)),
                ('Twitter', models.URLField(blank=True, help_text='Twitter url', null=True)),
                ('Instagram', models.URLField(blank=True, help_text='Instagram url', null=True)),
                ('linkedIn', models.URLField(blank=True, help_text='Linkedin url', null=True)),
                ('Address', models.CharField(blank=True, help_text='Your Address', max_length=1000, null=True)),
                ('Tel', models.IntegerField(blank=True, help_text='Your phone number', null=True)),
                ('Email', models.EmailField(blank=True, help_text='Your Email Address', max_length=254, null=True)),
                ('Working_hours', models.CharField(blank=True, help_text='Your specific working hours', max_length=300, null=True)),
            ],
        ),
    ]
