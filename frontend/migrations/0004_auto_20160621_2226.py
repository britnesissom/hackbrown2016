# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20160621_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='address',
            new_name='listing_addr',
        ),
    ]
