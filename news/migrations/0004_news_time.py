# Generated by Django 3.1.2 on 2020-10-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201015_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]
