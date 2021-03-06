# Generated by Django 2.2.4 on 2020-08-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_auto_20200822_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
