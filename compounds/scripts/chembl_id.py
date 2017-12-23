import os
import xlrd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'yatcm.settings')
import django
django.setup()

from compounds.models import ChEMBL, Compound

def chembl_extract(cell):
    cell = cell.replace("?", "").strip()
    chemblid_list = cell.split(',') if cell else []
    for chemblid in chemblid_list:
        yield chemblid


def upload_chemblid(row_number):
    print row_number
    row = table.row_values(row_number)
    chinese_name = row[1].strip()
    english_name = row[3].strip()
    smiles = row[5].strip()
    chemblids = chembl_extract(row[0])

    compound, create = Compound.objects.get_or_create(
        english_name=english_name,
        chinese_name=chinese_name,
        smiles=smiles
    )

    for chemid in chemblids:
        chembl, created = ChEMBL.objects.get_or_create(chembl_id=chemid)
        chembl.compound = compound
        chembl.save()



if __name__ == '__main__':
    compound_file = '/home/jianping/Desktop/second_version/new/34680_add_chemblid.xlsx'
    table = xlrd.open_workbook(compound_file).sheet_by_index(0)
    nrows = table.nrows
    for idx in range(1, nrows):
        upload_chemblid(idx)
    print "Done!!!"

