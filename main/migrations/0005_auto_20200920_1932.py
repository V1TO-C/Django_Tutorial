# Generated by Django 3.1.1 on 2020-09-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200920_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='zt',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
