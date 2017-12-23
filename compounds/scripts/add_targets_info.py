import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()
from compounds.models import *
from compounds.models import Target

def uplaod_targets(line):
    '''There is some tcmid_idx, that is not in yatcm, so, when storing the relationship,
    we need to use try'''

    tcmid_link = line['url']
    target_name = line['target_name'] if isinstance(line['target_name'], str) else ''
    gene_name = line['gene']
    uniprot_name = line['uniprotid']
    uniprot_link = line['uniprot_link']
    related_ingredients = line['related_ingredient_info'].split('\n') if isinstance(line['related_ingredient_info'], str) else []

    target, created = Target.objects.get_or_create(
        target_name=target_name,
        gene_name=gene_name,
        uniprot_name=uniprot_name,
        tcmid_link=tcmid_link,
        uniprot_link=uniprot_link
    )

    for ingredient in related_ingredients:
        try:
            idx = int(ingredient.split('/')[-2])
            compound = Compound.objects.get(tcmid_idx=idx)
            target.compounds.add(compound)
            target.save()
        except:
            print 'tcmid_ingredient_index' + ':' + str(idx)


if __name__ == '__main__':
    targets_file = '/home/jianping/data/merged/data_base_result/new_hanle_source/remend/tcmid/related_targets.csv'
    target_df = pd.read_csv(targets_file)
    for idx, row in target_df.iterrows():
        print idx
        uplaod_targets(row)
    print 'Done!!!'

