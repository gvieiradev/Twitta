# Generated by Django 3.1.2 on 2021-02-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20210205_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='batman.png', upload_to='perfil-edit'),
        ),
    ]
