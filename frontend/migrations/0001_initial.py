# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 23:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rooms', models.SmallIntegerField()),
                ('bathrooms', models.SmallIntegerField()),
                ('comments', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cleanliness', models.SmallIntegerField()),
                ('heating', models.SmallIntegerField()),
                ('appliances', models.SmallIntegerField()),
                ('bathrooms', models.SmallIntegerField()),
                ('rooms', models.SmallIntegerField()),
                ('ll_avail', models.SmallIntegerField()),
                ('ll_helpful', models.SmallIntegerField()),
                ('ll_personality', models.SmallIntegerField()),
                ('comments', models.TextField(null=True)),
                ('listing_id', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
