import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import *

def upload_cls_info(line):
    cid = line['cid']
    first_Chinese = line['first_Chinese'].strip()
    second_Chinese = line['second_Chinese'].strip()
    first_English = line['first_English'].strip()
    second_English = line['second_English'].strip()

    try:
        cid = CID.objects.get(cid=cid)
        compound = cid.compound
        compound.first_Chinese_catogary = first_Chinese
        compound.second_Chinese_catogary = second_Chinese
        compound.first_English_catogary = first_English
        compound.second_English_catogary = second_English
        compound.save()
    except:
        print 'falled' + ':' + str(cid)

if __name__ == '__main__':
    cls_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/ten_book_class_1.xlsx'
    cls_df = pd.read_excel(cls_file)
    for idx, row in cls_df.iterrows():
        print idx
        upload_cls_info(row)
