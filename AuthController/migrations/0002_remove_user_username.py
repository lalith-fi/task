# Generated by Django 3.2 on 2021-07-28 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthController', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
