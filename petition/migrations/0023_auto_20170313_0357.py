# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-13 03:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0022_auto_20170313_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]