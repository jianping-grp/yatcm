import os
import xlrd
import pandas as pd


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import ChEMBL, ChEMBL_Assay_id

def assay_id_extract(cell):
    cells = cell.split(',') if cell else []
    for assay in cells:
        yield assay

def upload_assay_id(row):
    struc_chembl_id = row['chembl_id']
    assays = assay_id_extract(row['activti_chembl_id'])
    struc_chembl = ChEMBL.objects.get(chembl_id=struc_chembl_id)

    for assay in assays:
        assay_el, created = ChEMBL_Assay_id.objects.get_or_create(assay_id=assay)
        assay_el.chembl_id = struc_chembl
        assay_el.save()


if __name__ == '__main__':
    chembl_file = '/home/jianping/Desktop/second_version/new/chembl_info.csv'
    df = pd.read_csv(chembl_file)
    for idx, line in df.iterrows():
        print idx
        upload_assay_id(line)
