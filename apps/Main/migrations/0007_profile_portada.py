# Generated by Django 3.1.2 on 2021-02-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20210205_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='portada',
            field=models.FileField(default='batman.png', upload_to=''),
        ),
    ]