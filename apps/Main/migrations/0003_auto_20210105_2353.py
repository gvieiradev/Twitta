# Generated by Django 3.1.2 on 2021-01-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biografia',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social',
            field=models.TextField(blank=True),
        ),
    ]