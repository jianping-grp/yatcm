# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0089_remove_compound_chembls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chembl',
            name='assay_chembl_ids',
        ),
        migrations.RemoveField(
            model_name='chembl',
            name='doc_chembl_ids',
        ),
        migrations.RemoveField(
            model_name='chembl',
            name='target_chembl_ids',
        ),
        migrations.DeleteModel(
            name='ChEMBL',
        ),
    ]
