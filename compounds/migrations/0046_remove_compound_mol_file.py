# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0045_auto_20171026_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='mol_file',
        ),
    ]
