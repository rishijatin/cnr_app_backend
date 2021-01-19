# Generated by Django 3.1.5 on 2021-01-19 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='healthCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Health Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('doctor_photo', models.URLField()),
                ('experience', models.IntegerField(default=0)),
                ('qualification', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.healthcategory')),
            ],
            options={
                'ordering': ['doctor_name'],
            },
        ),
    ]
