# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0082_chembl_assay_chembl_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chembl',
            name='assay_chembl_ids',
        ),
    ]
