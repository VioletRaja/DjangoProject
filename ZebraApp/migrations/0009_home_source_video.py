# Generated by Django 5.0.6 on 2024-07-09 06:55

import ZebraApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0008_remove_home_source_top_header_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_source',
            name='video',
            field=models.FileField(null=True, upload_to=ZebraApp.models.getFileName),
        ),
    ]
