# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0007_chembl_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chembl',
            name='compound',
        ),
        migrations.AddField(
            model_name='chembl',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound'),
        ),
    ]
