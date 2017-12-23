import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')

import django
django.setup()

from compounds.models import ChEMBL
import pandas as pd

def upload_chembl_info(line):
    chembl_id = line['chembl_id']
    prodrug = line['prodrug']
    oral = line['oral']
    max_phase = line['max_phase']
    pref_name = line['pref_name']
    canonical_smiles = line['canonical_smiles']


    ChEMBL.objects.filter(chembl_id=chembl_id).update(
        prodrug=prodrug,
        oral=oral,
        max_phase=max_phase,
        pref_name=pref_name,
        canonical_smi=canonical_smiles
    )


if __name__ == '__main__':
    chembl_info_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/28063_chembl_info_1.csv'
    chembl_info_df = pd.read_csv(chembl_info_file)
    for idx, row in chembl_info_df.iterrows():
        print idx
        upload_chembl_info(row)
    print 'Done!!!'


