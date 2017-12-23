import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
import pandas as pd

from compounds.models import *
from compounds.models import ChEMBL

def upload_similar_chembl(line):
    id = line['id']
    chembl_id_list = line['chembl_id'].split('\n') if line['chembl_id'] else []
    tanimoto_list = line['tanimoto_sml'].split('\n') if line['tanimoto_sml'] else []

    chembl_info_list = zip(chembl_id_list, tanimoto_list)

    compound = Compound.objects.get(id=id)
    for chembl_info in chembl_info_list:
        # store_chembls = list(compound.chembls.all())
        #
        chembl_id = chembl_info[0]
        tanimoto = chembl_info[1]
        if compound.chembls.filter(chembl_id=chembl_id):
            continue
        else:
            chembl_object, created = ChEMBL.objects.get_or_create(
                chembl_id=chembl_id,
                tanimoto=tanimoto,
                same_or_similar='similar'
            )
            compound.chembls.add(chembl_object)
            compound.save()


if __name__ == '__main__':
    similar_chembl = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/23332_structure_chembl_1.csv'
    similar_chembl_df = pd.read_csv(similar_chembl)

    for idx, row in similar_chembl_df.iterrows():
        print idx
        upload_similar_chembl(row)
    print 'Done!!!'



