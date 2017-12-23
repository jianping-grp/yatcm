# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0058_auto_20171031_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompoundFirstCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chinese_first_catagory', models.CharField(blank=True, max_length=1024, null=True)),
                ('English_first_catagory', models.CharField(blank=True, max_length=1024, null=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
            ],
        ),
        migrations.CreateModel(
            name='CompoundSecondCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chinese_second_catagory', models.CharField(blank=True, max_length=1024, null=True)),
                ('English_second_catagory', models.CharField(blank=True, max_length=1024, null=True)),
                ('catagory_smile', models.CharField(blank=True, max_length=1024, null=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
            ],
        ),
    ]
