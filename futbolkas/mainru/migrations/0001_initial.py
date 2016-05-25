# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category ')),
                ('alias', models.SlugField(verbose_name='alias  Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category ',
            },
        ),
        migrations.CreateModel(
            name='Itemru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name von Ware')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('image', models.CharField(max_length=255, verbose_name='Image')),
                ('alias', models.SlugField(verbose_name='alias  category')),
                ('categoryru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainru.Categoryru')),
            ],
            options={
                'verbose_name_plural': 'Name von Waren',
                'verbose_name': 'Name von Ware ',
            },
        ),
    ]