import os
import xlrd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
# from compounds.models import Compound, Herb, CID, CAS
from compounds.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s-[%(message)s]",
    filename='/home/jianping/django_test/logs/compound_log.txt',
    filemode='w'
)

def extract_cids(cell):
    return [int(float(x)) for x in cell.split('\n')] if cell else []

def herbs_extract(cell):
    cell = cell.replace("?", '').strip()
    herbs = cell.split('\n') if cell else []
    for herb in herbs:
        yield herb.split(';')

def upload_compound(row_number):
    print row_number
    row = table.row_values(row_number)
    chinese_name = row[0].strip()
    chinese_synonyms = row[1].split('\n') if row[1] else []
    english_name = row[2].strip()
    english_synonyms = row[3].split('\n') if row[3] else []
    smiles = row[4].strip()
    herbs = herbs_extract(row[7])
    cids = extract_cids(row[5])
    cass = row[6].split('\n') if row[6] else []

    compound, created = Compound.objects.get_or_create(
        english_name=english_name,
        chinese_name=chinese_name,
        smiles=smiles
    )

    for cn_identity in chinese_synonyms:
        chinese_identity, created = ChineseIdentity.objects.get_or_create(identity=cn_identity)
        chinese_identity.compound = compound
        chinese_identity.save()

    for en_identity in english_synonyms:
        english_identity, created = EnglishIdentity.objects.get_or_create(identity=en_identity)
        english_identity.compound = compound
        english_identity.save()

    for cid in cids:
        try:
            c, created = CID.objects.get_or_create(cid=cid)
            c.compound = compound
            c.save()
        except CID.DoesNotExist:
            logging.warning("{} Does not find in the CID database".format(cid))
        except CID.MultipleObjectsReturned:
            logging.warning("{} find multiple cid objs in database".format(cid))

    for cas in cass:
        try:
            ca, created = CAS.objects.get_or_create(cas=cas)
            ca.compound = compound
            ca.save()
        except CAS.DoesNotExist:
            logging.warning("{} Does not find in the CAS database".format(cas))
        except CAS.MultipleObjectsReturned:
            logging.warning("{} find multiple cas objs in database".format(cas))

    for herb in herbs:
        try:
            h, created = Herb.objects.get_or_create(Chinese_name=herb[0], English_name=herb[1])
            h.compounds.add(compound)
            h.save()
        except Herb.DoesNotExist:
            logging.info("Can not find %s, %s in databasecuo" % (herb[0], herb[1]))
        except Herb.MultipleObjectsReturned:
            logging.info("return multiple herbs %s, %s" % (herb[0], herb[1]))





if __name__ == '__main__':
    compound_file = '/home/jianping/Desktop/second_version/new/34680_res.xlsx'
    table = xlrd.open_workbook(compound_file).sheet_by_index(0)
    nrows = table.nrows
    map(upload_compound, range(1, nrows))
    print("Done!!!")
