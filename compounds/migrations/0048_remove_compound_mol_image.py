# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0047_compound_mol_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='mol_image',
        ),
    ]
