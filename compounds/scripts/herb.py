import os
import xlrd
import logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'yatcm.settings')
import django
django.setup()
from compounds.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

logging.basicConfig(
    level=logging.WARNING,
    format='[%(message)s]',
    filename='/home/jianping/django_test/logs/herb_log.txt',
    filemode='w'
)

def upload_herb(row_number):
    print row_number
    row = table.row_values(row_number)
    chinese_name = row[1].strip()
    pinyin_name = row[2].strip()
    english_name = row[3].strip()
    latin_name = row[4].strip()
    first_catagory_chinese = row[5].strip()
    first_catagory_english = row[6].strip()
    second_catagory_chinese = row[7].strip()
    second_catagory_english=row[8].strip()
    use_part = row[9].strip()
    drug_property = row[10].strip()
    meridians = row[11].strip()
    effect = row[12].strip()
    indication = row[13].strip()
    wiki_english = row[14].strip() if row[14].strip() else row[15].strip()
    wiki_chinese = row[16].strip()
    source_id = row[24].strip()
    # related_id = row[25].strip()


    herb, created = Herb.objects.get_or_create(
        Chinese_name=chinese_name,
        pinyin_name=pinyin_name,
        English_name=english_name,
        latin_name=latin_name,
        first_catagory_chinese=first_catagory_chinese,
        first_catagory_english=first_catagory_english,
        second_catagory_chinese=second_catagory_chinese,
        second_catagory_english=second_catagory_english,
        use_part=use_part,
        effect=effect,
        indication=indication,
        meridians=meridians,
        drug_property=drug_property,
        source_id=source_id,
        wiki_chinese=wiki_chinese,
        wiki_english=wiki_english,

    )



    if row[17]:
        tax_id = row[17]
    else:
        tax_id = row[19]

    if tax_id and tax_id != '':
        try:
            tax_id = int(float(tax_id))
            # print tax_id
            try:
                taxonomy, created = TCMTaxonomy.objects.get_or_create(taxonomy_id=tax_id)
                # taxonomy.save()
                herb.taxonomy = taxonomy
                herb.save()
            except ObjectDoesNotExist:
                logging.warning("Can not find {} in database".format(tax_id))
            except MultipleObjectsReturned:
                logging.warning("Multiple taxonomy with ID {} find in database".format(tax_id))
        except ValueError:
            logging.debug("{} can not convert to integer".format(tax_id))
    # try:
    #     h, created = Herb.objects.get_or_create(source_id=related_id)
    #     h.related_herbs = herb
    #     h.save()
    # except:
    #     logging.info("This model have bugs")

def upload_related_herbs(row_number):
    print row_number
    row = table.row_values(row_number)
    chinese_name = row[1].strip()
    pinyin_name = row[2].strip()
    english_name = row[3].strip()
    latin_name = row[4].strip()
    first_catagory_chinese = row[5].strip()
    first_catagory_english = row[6].strip()
    second_catagory_chinese = row[7].strip()
    second_catagory_english=row[8].strip()
    use_part = row[9].strip()
    drug_property = row[10].strip()
    meridians = row[11].strip()
    effect = row[12].strip()
    indication = row[13].strip()
    wiki_english = row[14].strip() if row[14].strip() else row[15].strip()
    wiki_chinese = row[16].strip()
    source_id = row[24].strip()
    related_id = row[25].strip()

    herb = Herb.objects.get(
        Chinese_name=chinese_name,
        pinyin_name=pinyin_name,
        English_name=english_name,
        latin_name=latin_name,
        first_catagory_chinese=first_catagory_chinese,
        first_catagory_english=first_catagory_english,
        second_catagory_chinese=second_catagory_chinese,
        second_catagory_english=second_catagory_english,
        use_part=use_part,
        effect=effect,
        indication=indication,
        meridians=meridians,
        drug_property=drug_property,
        source_id=source_id,
        wiki_chinese=wiki_chinese,
        wiki_english=wiki_english,

    )

    try:
        h = Herb.objects.get(source_id=related_id)
        herb.related_herbs = h
        herb.save()
    except ObjectDoesNotExist:
        logging.warning("Can not find {} in database".format(related_id))
    except MultipleObjectsReturned:
        logging.critical("Multiple taxonomy with Id {} find in database".format(related_id))



if __name__ == '__main__':
    herb_file = '/home/jianping/Desktop/second_version/new/7629_traditional_herbs_last_1.xlsx'
    # herb_file = '/home/jianping/Desktop/second_version/new/test.xlsx'
    table = xlrd.open_workbook(herb_file).sheet_by_index(0)
    nrows = table.nrows
    map(upload_herb, range(1, nrows))
    map(upload_related_herbs, range(1, nrows))
    print 'Done!!!'

