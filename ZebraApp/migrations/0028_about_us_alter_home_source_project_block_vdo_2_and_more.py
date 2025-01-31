# Generated by Django 5.0.6 on 2024-07-15 06:30

import ZebraApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0027_alter_project_site_pics_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(blank=True, max_length=10, null=True)),
                ('about_us_home', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='home_source',
            name='Project_Block_Vdo_2',
            field=models.FileField(blank=True, null=True, upload_to=ZebraApp.models.getFileName),
        ),
        migrations.AlterField(
            model_name='home_source',
            name='subject',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject will show under the logo'),
        ),
        migrations.AlterField(
            model_name='home_source',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=ZebraApp.models.getFileName, verbose_name='Upload a video to show in Slider'),
        ),
    ]
