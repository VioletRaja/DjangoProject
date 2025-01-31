# Generated by Django 5.0.6 on 2024-07-06 07:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0003_alter_contactus_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='username1',
        ),
        migrations.AddField(
            model_name='contactus',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='company',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=300),
        ),
    ]
