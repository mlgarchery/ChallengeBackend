# Generated by Django 3.1.2 on 2020-10-16 23:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=400)),
                ('refresh_token', models.CharField(max_length=400)),
                ('expires_in', models.IntegerField()),
                ('retrieved_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('external_urls', models.JSONField()),
                ('followers', models.JSONField()),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), size=None)),
                ('href', models.URLField()),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None)),
                ('name', models.CharField(max_length=300)),
                ('popularity', models.IntegerField()),
                ('type', models.CharField(max_length=300)),
                ('uri', models.CharField(max_length=300)),
                ('retrieved_date', models.DateTimeField()),
            ],
        ),
    ]
