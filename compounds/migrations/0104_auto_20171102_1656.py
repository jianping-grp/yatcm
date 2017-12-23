# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0103_auto_20171102_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='chembl',
            name='canonical_smi',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='chembl',
            name='max_phase',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='chembl',
            name='oral',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='chembl',
            name='pref_name',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='chembl',
            name='prodrug',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
