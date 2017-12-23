import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
import pandas as pd

# from compounds.models import *
from compounds.models import CompoundFirstCatagory, CompoundSecondCatagory

def uplaod_relationship(line):
    first_English = line['first_English'].strip()
    second_info_list = line['second_info'].split('\n') if line['second_info'] else []

    first_category_object = CompoundFirstCatagory.objects.get(English_first_catagory=first_English)

    for second_info in second_info_list:
        Chinese_name = second_info.split(':')[0].strip()
        English_name = second_info.split(':')[1].strip()
        second_category_object, created = CompoundSecondCatagory.objects.get_or_create(
            Chinese_second_catagory=Chinese_name,
            English_second_catagory=English_name
        )
        second_category_object.first_category = first_category_object
        second_category_object.save()


if __name__ == '__main__':
    relationship_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/first_and_second_category_relationship.xlsx'
    relation_df = pd.read_excel(relationship_file)
    for idx, row in relation_df.iterrows():
        # if idx == 6:
        uplaod_relationship(row)
    print 'Done!!!'

