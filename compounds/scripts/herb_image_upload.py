import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
import xlrd
from compounds.models import *
from django.core.files import File

base_dir = '/home/jianping/django_test/yatcm'
herb_image_dir = os.path.join(base_dir, 'media', 'herb_images')

def herb_upload(row_number):
    print row_number
    row = table.row_values(row_number)
    source_id = row[3].strip()
    chinese_name = row[5].strip()
    english_name = row[7].strip()
    suffix = row[1].strip()
    fix_chinese_name = row[2].strip()
    image_dir = row[0].strip()
    if image_dir:
        if fix_chinese_name:
            image_name = fix_chinese_name + '-*-' + english_name + '.' + suffix
        else:
            image_name = chinese_name + '-*-' + english_name + '.' + suffix

        herb = Herb.objects.get(source_id=source_id)
        img = File(open(image_dir))
        herb.image.save(image_name, img)
        herb.save()









if __name__ == '__main__':
    herb_file = '/home/jianping/Desktop/second_version/new/7629_traditional_herbs_last_1_add_pic.xlsx'
    table = xlrd.open_workbook(herb_file).sheet_by_index(0)
    nrows = table.nrows
    map(herb_upload, range(1, nrows))

