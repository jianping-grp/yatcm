# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0043_auto_20171026_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='mol_file',
        ),
        migrations.RemoveField(
            model_name='compound',
            name='mol_image',
        ),
    ]
