import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
import pandas as pd

from compounds.models import *
from compounds.models import ChEMBL

def upload_same_chemblid(line):
    index = line['id']
    chembl_id = line['chembl_id']
    chembl_object, created = ChEMBL.objects.get_or_create(chembl_id=chembl_id, same_or_similar='same', tanimoto=1.0)
    compound = Compound.objects.get(id=index)
    compound.chembls.add(chembl_object)
    compound.save()

if __name__ == '__main__':
    chembl_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/yatcm_same_chembl_1.csv'
    chembl_df = pd.read_csv(chembl_file)
    for idx, row in chembl_df.iterrows():
        print idx
        upload_same_chemblid(row)
    print 'Done!!!'

