from rest_framework import serializers
from .models import *
from rest_framework_recursive.fields import RecursiveField

# __all__ = [
#     "ChineseIdentitySerializer",
#     "EnglishIdentitySerializer",
#     "CompoundSerializer",
#     # "StructureSerializer",
#     "HerbSerializer",
#     "ChEMBlSerializer",
#     "CASSerializer",
#     "CIDSerializer",
#     "TCMTaxonomySerializer",
#     "KEGGPathwayCategorySerializer",
#     "KEGGCompoundSerializer",
#     "KEGGPathwaySerializer",
#     "KEGGSimilaritySerializer",
#     "PrescriptionSerializer"
# ]


class ChineseIdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ChineseIdentity
        fields = "__all__"


class EnglishIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishIdentity
        fields = "__all__"


# class StructureSerializer(serializers.ModelSerializer):
#     compound = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Structure
#         exclude = ('mol', 'bfp', 'mol_block')
#         read_only_fields = ('formula', 'alogp', 'psa', 'rtb', 'mol_weight', 'hba', 'hbd')


class CompoundSerializer(serializers.ModelSerializer):
    herb_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    englisthidentity_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    chineseidentity_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Compound
        exclude = ('mol', 'bfp', 'mol_block')
        read_only_fields = ('formula', 'alogp', 'psa', 'rtb', 'mol_weight', 'hba', 'hbd')
        # depth =1     # nested depth


class HerbSerializer(serializers.ModelSerializer):
    prescription_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Herb
        # fields = "__all__"
        exclude = ['taxonomy']


class CIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CID
        fields = "__all__"


class CASSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAS
        fields = "__all__"


# class ChEMBlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChEMBL
#         fields = "__all__"


class TCMTaxonomySerializer(serializers.ModelSerializer):
    # children = serializers.ListField(read_only=True, child=RecursiveField())

    class Meta:
        model = TCMTaxonomy
        fields = "__all__"
        # exclude = ['parent']


class KEGGCompoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGCompound
        fields = "__all__"


class KEGGPathwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGPathway
        fields = "__all__"


class KEGGSimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGSimilarity
        fields = "__all__"


class KEGGPathwayCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGPathwayCategory
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
