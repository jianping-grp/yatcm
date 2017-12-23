# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 02:20
from __future__ import unicode_literals

import compounds.models
from django.db import migrations, models
import django.db.models.deletion
import django_rdkit.models.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cas', models.CharField(blank=True, max_length=1024, null=True, verbose_name='CAS Registry Number')),
                ('url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='URL link to chemfinder database')),
            ],
            options={
                'verbose_name_plural': 'CAS',
            },
        ),
        migrations.CreateModel(
            name='ChineseIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.BigIntegerField(blank=True, null=True, verbose_name='PubChem Compound Identification')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to PubChem.')),
            ],
            options={
                'verbose_name_plural': 'CID',
            },
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(max_length=2012)),
                ('smiles', models.CharField(blank=True, max_length=1024)),
                ('mol', django_rdkit.models.fields.MolField(blank=True, null=True)),
                ('mol_block', models.TextField(blank=True)),
                ('mol_file', models.FileField(blank=True, null=True, upload_to='mol_files/')),
                ('mol_image', models.ImageField(blank=True, null=True, upload_to='mol_images/')),
                ('first_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('formula', models.CharField(blank=True, max_length=1024)),
                ('mol_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('alogp', models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='Calculated AlogP')),
                ('hba', models.SmallIntegerField(blank=True, null=True, verbose_name='Number hydrogen bond acceptors')),
                ('hbd', models.SmallIntegerField(blank=True, null=True, verbose_name='Number hydrogen bond donors')),
                ('psa', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Polar surface area')),
                ('rtb', models.SmallIntegerField(blank=True, null=True, verbose_name='Number rotatable bonds')),
                ('related_compounds', models.ManyToManyField(blank=True, related_name='_compound_related_compounds_+', to='compounds.Compound')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='EnglishIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=1024)),
                ('compound', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chinese_name', models.CharField(blank=True, max_length=1024)),
                ('pinyin_name', models.CharField(blank=True, max_length=1024)),
                ('English_name', models.CharField(blank=True, max_length=1024)),
                ('latin_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('first_catagory_chinese', models.CharField(blank=True, max_length=1024)),
                ('first_catagory_english', models.CharField(blank=True, max_length=1024)),
                ('second_catagory_chinese', models.CharField(blank=True, max_length=1024)),
                ('second_catagory_english', models.CharField(blank=True, max_length=1024)),
                ('image', models.ImageField(blank=True, null=True, upload_to='herb_images')),
                ('wiki_english', models.URLField(blank=True)),
                ('wiki_chinese', models.URLField(blank=True)),
                ('drug_property', models.CharField(blank=True, max_length=1024, null=True)),
                ('meridians', models.CharField(blank=True, max_length=1024, null=True)),
                ('use_part', models.CharField(blank=True, max_length=1024, null=True)),
                ('effect', models.CharField(blank=True, max_length=1024, null=True)),
                ('indication', models.CharField(blank=True, max_length=1024, null=True)),
                ('source_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
                ('related_herbs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Herb')),
            ],
        ),
        migrations.CreateModel(
            name='KEGGCompound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegg_id', models.CharField(max_length=64, verbose_name='KEGG ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('mol', django_rdkit.models.fields.MolField(blank=True, null=True, verbose_name='An RDKit molecule')),
                ('mol_block', models.TextField(blank=True, null=True, verbose_name='Mol block')),
                ('smiles', models.TextField(blank=True, max_length=1024, null=True)),
                ('mol_image', models.ImageField(blank=True, null=True, storage=compounds.models.OverwirteStorage, upload_to='mol_image/')),
            ],
        ),
        migrations.CreateModel(
            name='KEGGPathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegg_id', models.CharField(max_length=64, verbose_name='KEGG ID')),
                ('name', models.CharField(max_length=128)),
                ('kgml', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, storage=compounds.models.OverwirteStorage, upload_to='kegg_pathway_image/')),
            ],
        ),
        migrations.CreateModel(
            name='KEGGPathwayCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='compounds.KEGGPathwayCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KEGGSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(blank=True, null=True)),
                ('kegg_compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.KEGGCompound')),
                ('tcm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('english_name', models.CharField(blank=True, max_length=1024)),
                ('pinyin_name', models.CharField(blank=True, max_length=1024)),
                ('zucheng', models.TextField(blank=True)),
                ('yongfa', models.TextField(blank=True)),
                ('fangjie', models.TextField(blank=True)),
                ('chinese_indiction', models.TextField(blank=True)),
                ('english_indiction', models.TextField(blank=True)),
                ('chinese_modern_application', models.TextField(blank=True)),
                ('english_modern_application', models.TextField(blank=True)),
                ('herbs', models.ManyToManyField(to='compounds.Herb')),
                ('main_prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Prescription')),
            ],
        ),
        migrations.CreateModel(
            name='TCMTaxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('pinyin_name', models.CharField(blank=True, max_length=1024)),
                ('taxonomy_id', models.BigIntegerField(blank=True, null=True)),
                ('ncbi_link', models.URLField(blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='compounds.TCMTaxonomy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='keggpathway',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.KEGGPathwayCategory'),
        ),
        migrations.AddField(
            model_name='keggcompound',
            name='pathway',
            field=models.ManyToManyField(to='compounds.KEGGPathway'),
        ),
        migrations.AddField(
            model_name='keggcompound',
            name='similar_to_tcm',
            field=models.ManyToManyField(through='compounds.KEGGSimilarity', to='compounds.Compound'),
        ),
        migrations.AddField(
            model_name='herb',
            name='taxonomy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.TCMTaxonomy'),
        ),
        migrations.AddField(
            model_name='cid',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cid', to='compounds.Compound'),
        ),
        migrations.AddField(
            model_name='chineseidentity',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound'),
        ),
        migrations.AddField(
            model_name='cas',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cas', to='compounds.Compound'),
        ),
    ]
