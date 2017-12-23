import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')

import django
django.setup()
import pandas as pd
from compounds.models import ChEMBL, Assay_Chembl_id, Doc_Chembl_id, Target_Chembl_id

def upload_chembl_relationship(line):
    chembl_id = line['chembl_id']
    assay_chembl_id_list = line['assay_chembl_id'].split(', ') if isinstance(line['assay_chembl_id'], str) else []
    doc_chembl_id_list = line['doc_chembl_id'].split(', ') if isinstance(line['doc_chembl_id'], str) else []
    target_chembl_id_list = line['target_chembl_id'].split(', ') if isinstance(line['target_chembl_id'], str) else []

    chembl_object_list = ChEMBL.objects.filter(chembl_id=chembl_id)
    for chembl_object in chembl_object_list:
        for assay_chembl_id in assay_chembl_id_list:
            assay_chembl_object, created = Assay_Chembl_id.objects.get_or_create(assay_chembl_id=assay_chembl_id)
            chembl_object.assay_chembl_ids.add(assay_chembl_object)
            chembl_object.save()

        for doc_chembl_id in doc_chembl_id_list:
            doc_chembl_object, created = Doc_Chembl_id.objects.get_or_create(doc_chembl_id=doc_chembl_id)
            chembl_object.doc_chembl_ids.add(doc_chembl_object)
            chembl_object.save()

        for target_chembl_id in target_chembl_id_list:
            target_chembl_object, created = Target_Chembl_id.objects.get_or_create(target_chembl_id=target_chembl_id)
            chembl_object.target_chembl_ids.add(target_chembl_object)
            chembl_object.save()


if __name__ == '__main__':
    chembl_relationship_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/28063_chembl_info_1.csv'
    df = pd.read_csv(chembl_relationship_file)
    for idx, row in df.iterrows():
        print idx
        upload_chembl_relationship(row)
    print 'Done!!!'


