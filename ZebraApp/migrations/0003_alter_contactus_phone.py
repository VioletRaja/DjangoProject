# Generated by Django 5.0.6 on 2024-07-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0002_rename_username_contactus_username1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
