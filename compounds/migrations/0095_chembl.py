# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0094_auto_20171102_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChEMBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chembl_id', models.CharField(blank=True, max_length=1024, null=True, verbose_name='ChEMBL ID')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to ChEMBL database')),
                ('canonical_smi', models.CharField(blank=True, max_length=1024, null=True)),
                ('max_phase', models.SmallIntegerField(blank=True, null=True)),
                ('prodrug', models.SmallIntegerField(blank=True, null=True)),
                ('oral', models.SmallIntegerField(blank=True, null=True)),
                ('pref_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('tanimoto', models.FloatField(blank=True, null=True)),
                ('same_or_similar', models.CharField(blank=True, max_length=200, null=True)),
                ('assay_chembl_ids', models.ManyToManyField(blank=True, to='compounds.Assay_Chembl_id')),
                ('doc_chembl_ids', models.ManyToManyField(blank=True, to='compounds.Doc_Chembl_id')),
                ('target_chembl_ids', models.ManyToManyField(blank=True, to='compounds.Target_Chembl_id')),
            ],
            options={
                'verbose_name_plural': 'ChEMBL ID',
            },
        ),
    ]
