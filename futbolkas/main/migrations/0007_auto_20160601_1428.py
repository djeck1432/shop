# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160530_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=1000, verbose_name='Photo link'),
        ),
    ]