# Generated by Django 5.0.6 on 2024-07-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZebraApp', '0015_home_source_utube_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='home_source',
            name='utube_link',
        ),
    ]
