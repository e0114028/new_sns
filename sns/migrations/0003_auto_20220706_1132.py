# Generated by Django 3.0.4 on 2022-07-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
