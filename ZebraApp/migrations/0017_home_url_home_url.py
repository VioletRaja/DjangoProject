# Generated by Django 5.0.6 on 2024-07-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0016_home_url_remove_home_source_utube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_url',
            name='home_url',
            field=models.URLField(blank=True, help_text='Enter the URL of the website', verbose_name='Web site utube link URL'),
        ),
    ]
