import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatcm.settings')
import django
django.setup()

from rdkit.Chem import Draw
from compounds.models import Compound
from django.core.files import File

BASE__DIR = '/home/jianping/django_test/yatcm'
IMAGE_DIR = os.path.join(BASE__DIR, 'media', 'mol_images')
MOL_DIR = os.path.join(BASE__DIR, 'media', 'mol_files')

def mol_plotter():
    if not os.path.isdir(BASE__DIR):
        os.mkdir(BASE__DIR)
    if not os.path.isdir(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    if not os.path.isdir(MOL_DIR):
        os.makedirs(MOL_DIR)

    compounds = Compound.objects.exclude(mol=None)
    for compound in compounds:
        image_name = '%s.svg' % compound.pk
        image_file = os.path.join(IMAGE_DIR, image_name)
        print image_file
        if not os.path.exists(image_file):
            Draw.MolToFile(compound.mol, image_file)
        img = File(open(image_file))
        compound.mol_image.save(image_name, img)

        mol_file_name = "%s.mol" % compound.pk
        mol_file = os.path.join(MOL_DIR, mol_file_name)
        print mol_file
        if not os.path.exists(mol_file):
            f = open(mol_file, 'w')
            f.write(compound.mol_block)
            f.close()
        mol_f = File(open(mol_file))
        compound.mol_file.save(mol_file_name, mol_f)
        compound.save()

if __name__ == '__main__':
    mol_plotter()
