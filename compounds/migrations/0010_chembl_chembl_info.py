# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0009_auto_20171001_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChEMBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chembl_id', models.CharField(blank=True, max_length=1024, null=True, verbose_name='ChEMBL ID')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to ChEMBL database')),
                ('compound', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound')),
            ],
            options={
                'verbose_name_plural': 'ChEMBL ID',
            },
        ),
        migrations.CreateModel(
            name='ChEMBL_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonical_smi', models.CharField(blank=True, max_length=1024, null=True)),
                ('max_phase', models.SmallIntegerField(blank=True, null=True)),
                ('prodrug', models.SmallIntegerField(blank=True, null=True)),
                ('oral', models.SmallIntegerField(blank=True, null=True)),
                ('pref_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('tanimoto', models.FloatField(blank=True, null=True)),
                ('activity_id', models.IntegerField(blank=True, null=True)),
                ('activity_chembl_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('chembl_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.ChEMBL')),
            ],
        ),
    ]
