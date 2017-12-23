import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import *
from compounds.models import CompoundFirstCatagory, CompoundSecondCatagory

def upload_catagory_info(line):
    foreign_id = line['id']
    English_name = line['English_name']
    Chinese_name = line['Chinese_name']
    smile = line['smiles']
    reference_smile = line['reference_structure'].split('\n') if line['reference_structure'] else []
    first_English_catagory = line['first_English_catagory'].split('\n') if line['first_English_catagory'] else []
    first_Chinese_catagory = line['first_Chinese_catagory'].split('\n') if line['first_Chinese_catagory'] else []
    second_English_catagory = line['second_English_catagory'].split('\n') if line['second_English_catagory'] else []
    second_Chinese_catagory = line['second_Chinese_catagory'].split('\n') if line['second_Chinese_catagory'] else []
    first_class_info = zip(first_Chinese_catagory, first_English_catagory)
    second_class_info = zip(second_Chinese_catagory, second_English_catagory, reference_smile)

    compound = Compound.objects.get(id=foreign_id)

    for first_class in first_class_info:
        Chinese_class = first_class[0]
        English_class = first_class[1]
        first_class_object, created = CompoundFirstCatagory.objects.get_or_create(
            Chinese_first_catagory=Chinese_class,
            English_first_catagory=English_class
        )
        first_class_object.compounds.add(compound)
        first_class_object.save()

    for second_class in second_class_info:
        Chinese_class = second_class[0]
        English_class = second_class[1]
        smile = second_class[2]
        second_class_object, create = CompoundSecondCatagory.objects.get_or_create(
            Chinese_second_catagory=Chinese_class,
            English_second_catagory=English_class,
            catagory_smile=smile
        )
        second_class_object.compounds.add(compound)
        second_class_object.save()


if __name__ == '__main__':
    catagory_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/classification_infomation.xlsx'
    catagory_df = pd.read_excel(catagory_file)
    for idx, row in catagory_df.iterrows():
        print idx
        upload_catagory_info(row)
