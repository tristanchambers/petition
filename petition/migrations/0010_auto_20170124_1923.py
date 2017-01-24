# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0009_auto_20170124_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signature',
            old_name='show_name',
            new_name='dont_show_name',
        ),
        migrations.AlterField(
            model_name='petition',
            name='hero_image',
            field=models.URLField(default=''),
        ),
    ]
