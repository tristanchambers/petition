# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-09 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0020_auto_20170204_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='thank_you_message',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]