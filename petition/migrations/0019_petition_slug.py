# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-04 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0018_auto_20170129_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
