# Generated by Django 2.2.4 on 2020-08-24 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
