# Generated by Django 2.2.4 on 2020-08-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.CharField(max_length=10),
        ),
    ]