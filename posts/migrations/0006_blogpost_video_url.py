# Generated by Django 3.1.5 on 2021-02-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210125_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='video_url',
            field=models.URLField(default='https://www.google.com'),
            preserve_default=False,
        ),
    ]
