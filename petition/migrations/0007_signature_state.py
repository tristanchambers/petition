# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0006_petition_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
