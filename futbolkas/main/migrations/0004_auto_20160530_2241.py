# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160525_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forma',
            options={'verbose_name': 'Форма оплаты', 'verbose_name_plural': 'Формы оплаты'},
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
    ]
