# Generated by Django 3.1.5 on 2021-02-12 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='EmploymentNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('details', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employment.category')),
            ],
            options={
                'verbose_name_plural': 'Employment News',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='employment.employmentnews')),
            ],
        ),
    ]
