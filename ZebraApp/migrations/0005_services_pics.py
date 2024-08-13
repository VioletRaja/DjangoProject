# Generated by Django 5.0.6 on 2024-07-08 06:12

import ZebraApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0004_remove_contactus_username1_contactus_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='services_pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=ZebraApp.models.getFileName)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
            ],
        ),
    ]
