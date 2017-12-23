import os
import xlrd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import *
from compounds.models import TCMID_Herbs, Compound_MS

def upload_new_compound(row_number):
    print row_number
    row = table.row_values(row_number)
    tcmid_idx = row[4]
    smile = row[0].strip()
    cid_list = row[1].split('\n') if row[1] else []
    herb_list = row[2].split('\n') if row[2] else []
    ms_link = row[3].split('\n') if row[3] else []

    compound = Compound.objects.get(smiles=smile)
    compound.tcmid_idx = tcmid_idx
    compound.save()
    # for cid in cid_list:
    #     cid_object, created = CID.objects.get_or_create(cid=int(cid))
    #     cid_object.compound = compound
    #     cid_object.save()
    #
    # for herb in herb_list:
    #     try:
    #         temp_list = herb.split(':')
    #         http_index = temp_list.index('http')
    #         English_name = ':'.join(temp_list[:http_index])
    #         tcmid_link = ':'.join(temp_list[http_index:])
    #         # tcmid_link = temp_list[1] + ':' + temp_list[2]
    #         tcmid_herb, created = TCMID_Herbs.objects.get_or_create(English_name=English_name, tcmid_link=tcmid_link)
    #         tcmid_herb.compounds.add(compound)
    #         tcmid_herb.save()
    #     except ValueError:
    #         print
    #
    # for link in ms_link:
    #     link_object, created = Compound_MS.objects.get_or_create(ms_link=link)
    #     link_object.compound = compound
    #     link_object.save()

if __name__ == '__main__':
    compound_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/tcmid/rm_similar_cid_and_structure.xlsx'
    table = xlrd.open_workbook(compound_file).sheet_by_index(0)
    nrows = table.nrows
    map(upload_new_compound, range(1, nrows))
    print 'Done!!!'
