# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0059_compoundfirstcatagory_compoundsecondcatagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compoundfirstcatagory',
            name='compounds',
        ),
        migrations.RemoveField(
            model_name='compoundsecondcatagory',
            name='compounds',
        ),
        migrations.DeleteModel(
            name='CompoundFirstCatagory',
        ),
        migrations.DeleteModel(
            name='CompoundSecondCatagory',
        ),
    ]