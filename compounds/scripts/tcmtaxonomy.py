import os
import re
import time
import logging
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'yatcm.settings')
import django
django.setup()
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from compounds.models import *

names_file = '/home/jianping/Desktop/second_version/taxdump/names.dmp'
nodes_file = '/home/jianping/Desktop/second_version/taxdump/nodes.dmp'

herb_file = '/home/jianping/Desktop/second_version/new/7629_traditional_herbs_last_1.xlsx'
taxonomy_file = '/home/jianping/Desktop/second_version/taxdump/taxonomy.txt'

logger = logging.getLogger('tax_logger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/home/jianping/django_test/logs/tax_log.txt')
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

"""upload taxonomy using pandas"""

def get_tax(file_name):
    with open(file_name) as f:
        for row in f:
            yield int(row.strip())

def get_sci_name(names_data, node):
    return names_data[(names_data[0] == node) & (names_data[3] == 'scientific name')].iloc[0][1]

def get_parent_id(nodes_data, node):
    return nodes_data[nodes_data[0] == node].iloc[0][1]

def get_family(nodes_data, child_node):
    family = [child_node]
    while family[-1] != 1:
        family.append(get_parent_id(nodes_data, child_node))
        child_node = get_parent_id(nodes_data, child_node)
    return family

if __name__ == '__main__':
    start = time.clock()
    nodes = pd.read_table(nodes_file, header=None, sep=r'\t\|\t', usecols=range(12))
    read_nodes = time.clock()
    logger.info("read nodes spent {} s".format(read_nodes-start))

    names = pd.read_table(names_file, header=None, sep=r"\t\|\t|\t|", usecols=range(4))
    read_names = time.clock()
    logging.info("read names spent {} s".format(read_names - read_nodes))

    taxonomies = get_tax(taxonomy_file)

    for tax in taxonomies:
        print tax
        try:
            family = get_family(nodes, tax)
        except IndexError:
            logger.warning("{} get no data from database".format(tax))
            continue
        child = None
        for node in family:
            try:
                name = get_sci_name(names, node)
                taxonomy, created = TCMTaxonomy.objects.get_or_create(name=name, taxonomy_id=node)
                if child:
                    child.parent = taxonomy
                    child.save()
                child = taxonomy
                if not created:
                    break
            except TCMTaxonomy.MultipleObjectsReturned:
                logger.warning("{} returns more than one records.".format(node))






