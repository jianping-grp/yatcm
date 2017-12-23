import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')

import django
django.setup()

from compounds.models import *
from compounds.models import CompoundFirstCatagory, CompoundSecondCatagory
import pandas as pd

base_dir = '/home/jianping/Desktop/database_summary'

first_class_list = list(CompoundFirstCatagory.objects.all())
summary_dic = {}
for first_class in first_class_list:
    English_name = first_class.English_first_catagory
    module_sum = len(first_class.compounds.all())
    summary_dic[English_name] = module_sum
df = pd.Series(summary_dic, name='English_name')
print df
print type(df.plot.pie(figsize=(4, 4), fontsize=4, autopct='%.2f'))
# df.plot.pie(figsize=(4, 4), fontsize=4, autopct='%.2f').get_figure().savefig('/home/jianping/Desktop/test3.svg', format='svg')

# first_class_list = list(CompoundFirstCatagory.objects.all())
# summary_dic = {}
# temp_list = list()
# for first_class in first_class_list:
#     first_category_name = first_class.English_first_catagory
#     print first_category_name
#     second_class_list = list(first_class.compoundsecondcatagory_set.all())
#     for second_class in second_class_list:
#         English_name = second_class.English_second_catagory
#         module_sum = len(second_class.compounds.all())
#         summary_dic[English_name] = module_sum
#     series = pd.Series(summary_dic, name=first_category_name)
#     series.plot(kind='pie', figsize=(4, 4), fontsize=4, autopct='%.2f')
#     temp_list.append(series)
    # result_pic = os.path.join(base_dir, first_category_name+'.svg')
    # series.plot.pie(figsize=(4, 4), fontsize=4, autopct='%.2f').get_figure().savefig(result_pic)
# df = pd.DataFrame(temp_list)
# classification_summary_file = os.path.join(base_dir, 'classification_summary.xlsx')
# df.to_excel(classification_summary_file, sheet_name='Sheet1')



# temp_list = list()
#
# compound_list = list(Compound.objects.all())
# for compound in compound_list:
#     if compound.target_set.all():
#         temp_list.append(compound.english_name)
#
# print len(temp_list)



