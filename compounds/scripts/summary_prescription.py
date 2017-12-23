import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'yatcm.settings')
import django
django.setup()

from compounds.models import *

p = Prescription.objects.get(id=147)
# print p.herbs.all()
herbs_list = list(p.herbs.all())

compound_list = list()
for herb in herbs_list:
    # print len(herb.compounds.all())
    compound_list.extend(list(herb.compounds.all()))
print len(set(compound_list))


# temp_list = list()
# for el in compound_list:
#     if compound_list.count(el) != 1:
#         temp_list.append(el)
#
# print len(set(temp_list))


