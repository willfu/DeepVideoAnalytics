# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0013_auto_20170405_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='frame_index',
            field=models.IntegerField(unique=True),
        ),
    ]