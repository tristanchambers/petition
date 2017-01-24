# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0007_signature_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='region_city',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petition',
            name='region_state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
