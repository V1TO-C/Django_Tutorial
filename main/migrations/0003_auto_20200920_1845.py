# Generated by Django 3.1.1 on 2020-09-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='zt',
            field=models.TextField(default='-'),
        ),
    ]
