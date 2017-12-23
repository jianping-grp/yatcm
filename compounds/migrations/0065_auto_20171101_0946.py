# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0064_auto_20171101_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='similarchembl',
            name='compound',
        ),
        migrations.AddField(
            model_name='compound',
            name='similar_chembls',
            field=models.ManyToManyField(blank=True, to='compounds.SimilarChEMBL'),
        ),
    ]
