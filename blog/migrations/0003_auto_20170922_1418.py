# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170922_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='favorites_total',
            field=models.IntegerField(default=0, verbose_name='favorites_total'),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='blog.Article'),
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together=set([('article', 'id')]),
        ),
    ]
