# Generated by Django 5.0.6 on 2024-07-09 06:11

import ZebraApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0006_services_pics_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Top_Header_video', models.FileField(null=True, upload_to=ZebraApp.models.getFileName)),
                ('image', models.ImageField(null=True, upload_to=ZebraApp.models.getFileName)),
            ],
        ),
    ]
