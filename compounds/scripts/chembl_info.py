import os
import xlrd
import pandas as pd


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import ChEMBL

def assayid_extract(cell):
    assayid_list = cell.split(',') if cell else []
    for assyid in assayid_list:
        yield assyid

def upload_chembl_info(row):
    struc_chemblid = row['chembl_id']
    canonical_smiles = row['canonical_smiles']
    max_phase = row['max_phase']
    prodrug = row['prodrug']
    oral = row['oral']
    pref_name = row['pref_name']
    tanimoto = row['tanimoto']
    # assayids = assayid_extract(row['activity_chembl_id'])

    chemblinfo = ChEMBL.objects.get(
        chembl_id=struc_chemblid)
    chemblinfo.canonical_smi = canonical_smiles
    chemblinfo.max_phase = max_phase
    chemblinfo.prodrug = prodrug
    chemblinfo.oral = oral
    chemblinfo.pref_name = pref_name
    chemblinfo.tanimoto = tanimoto
    chemblinfo.save()



if __name__ == '__main__':
    compound_file = '/home/jianping/Desktop/second_version/new/chembl_info.csv'
    df = pd.read_csv(compound_file)
    # print df.ix[3]
    for idx, line in df.iterrows():
        upload_chembl_info(line)
