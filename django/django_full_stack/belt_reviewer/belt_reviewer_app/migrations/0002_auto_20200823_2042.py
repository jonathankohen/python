# Generated by Django 2.2.4 on 2020-08-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_reviewer_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wish_list_adds',
        ),
        migrations.AddField(
            model_name='item',
            name='favorites',
            field=models.ManyToManyField(related_name='items_favorited', to='belt_reviewer_app.User'),
        ),
    ]
