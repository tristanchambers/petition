# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-27 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0014_auto_20170127_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signature',
            old_name='street',
            new_name='street_address',
        ),
    ]
