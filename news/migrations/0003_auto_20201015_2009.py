# Generated by Django 3.1.2 on 2020-10-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201014_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]