# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0027_auto_20171025_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCMID_Herbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('English_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('tcmid_link', models.URLField(blank=True, max_length=2014, null=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
            ],
        ),
    ]
