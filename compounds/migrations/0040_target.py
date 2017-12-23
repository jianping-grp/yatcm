# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0039_auto_20171026_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_name', models.CharField(blank=True, max_length=2048, null=True)),
                ('gene_name', models.CharField(blank=True, max_length=2048, null=True)),
                ('uniprot_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('uniprot_link', models.URLField(blank=True, max_length=2048, null=True)),
                ('tcmid_link', models.URLField(blank=True, max_length=2048, null=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
                ('related_diseases', models.ManyToManyField(blank=True, to='compounds.Diseases')),
                ('related_drugs', models.ManyToManyField(blank=True, to='compounds.Drugs')),
            ],
        ),
    ]
