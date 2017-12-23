import os
import xlrd
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'yatcm.settings')
import django
django.setup()

from compounds.models import *

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

primary_file = '/home/jianping/Desktop/second_version/prescript_info/last/prescription_primary_complete_last.xlsx'
vice_file = '/home/jianping/Desktop/second_version/prescript_info/last/vice_complete.xlsx'

logger = logging.getLogger('tax_logger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/home/jianping/django_test/logs/prescription.txt')
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

def primary_upload(row):
    chinese_name = row[0].strip()
    english_name = row[1].strip()
    pinyin = row[2].strip()
    zucheng = row[3].strip()
    herb_list = row[3].strip().split()
    yongfa = row[4].strip()
    fangjie = row[5].strip()
    chinese_gongyong = row[6].strip()
    english_gongyong = row[7].strip()
    chinese_xiandai = row[8].strip()
    english_xiandai = row[9].strip()

    try:
        prescription, created = Prescription.objects.get_or_create(
            chinese_name=chinese_name,
            english_name=english_name,
            pinyin_name=pinyin,
            zucheng=zucheng,
            yongfa=yongfa,
            fangjie=fangjie,
            chinese_indiction=chinese_gongyong,
            english_indiction=english_gongyong,
            chinese_modern_application=chinese_xiandai,
            english_modern_application=english_xiandai
        )
    except Prescription.DoesNotExist:
        logger.warning("{} does not exist!".format(unicode(chinese_name)))
    except Prescription.MultipleObjectsReturned:
        logger.warning("{} return more than one objects".format(unicode(chinese_name)))

    for herb_name in herb_list:
        try:
            herbs = Herb.objects.filter(Chinese_name=herb_name)
            for herb in herbs:
                prescription.herbs.add(herb)
                prescription.save()
        except Herb.DoesNotExist:
            logger.info("{} does not exist".format(herb_name))

def vice_upload(row):
    main_prescription_name = row[0].strip()
    chinese_name = row[1].strip()
    pinyin_name = row[2].strip()
    zucheng = row[3].strip()
    herb_list = row[3].strip().split()
    yongfa = row[4].strip()

    try:
        prescription, created = Prescription.objects.get_or_create(
            chinese_name=chinese_name,
            pinyin_name=pinyin_name,
            zucheng=zucheng,
            yongfa=yongfa
        )

        try:
            main_prescription = Prescription.objects.get(chinese_name=main_prescription_name)
            prescription.main_prescription = main_prescription
            prescription.save()
        except Prescription.DoesNotExist:
            logger.warning("%s does not exist!" % main_prescription_name)
        except Prescription.MultipleObjectsReturned:
            logger.warning("%s return more than one objects" % main_prescription_name)

        for herb_name in herb_list:
            try:
                herbs = Herb.objects.filter(Chinese_name=herb_name)
                for herb in herbs:
                    prescription.herbs.add(herb)
                    prescription.save()
            except Herb.DoesNotExist:
                logger.info("{} does not exist".format(herb_name))

    except Prescription.DoesNotExist:
        logger.warning("%s does not exist".format(chinese_name))
    except Prescription.MultipleObjectsReturned:
        logger.warning("{} return more than one objects".format(chinese_name))


if __name__ == '__main__':
    primary_table = xlrd.open_workbook(primary_file).sheet_by_index(0)
    for row_number in range(1, primary_table.nrows):
        print row_number
        row = primary_table.row_values(row_number)
        primary_upload(row)
        # vice_upload(row)
    vice_table = xlrd.open_workbook(vice_file).sheet_by_index(0)
    for row_number in range(1, vice_table.nrows):
        print row_number
        row = vice_table.row_values(row_number)
        vice_upload(row)


