from . import models
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class ChEMBLNode(DjangoObjectType):
    class Meta:
        model = models.ChEMBL
        filter_fields = ['chembl_id', 'canonical_smi', 'pref_name']
        interfaces = (relay.Node, )


class CompoundNode(DjangoObjectType):
    # chembls = DjangoFilterConnectionField(ChEMBLNode)
    class Meta:
        model = models.Compound
        exclude_fields = (
            'mol',
            'bfp'
        )
        filter_fields = [
            'english_name',
            'chinese_name'
        ]
        interfaces = (relay.Node, )
    @classmethod
    def get_node(cls, info, id):
        try:
            cpd = cls._meta.model.objects.get(id=id)
        except cls._meta_model.DoesNotExist:
            return None
        return cpd   ### should be return None

class HerbNode(DjangoObjectType):
    compounds = DjangoFilterConnectionField(CompoundNode)
    class Meta:
        model = models.Herb
        filter_fields = ['Chinese_name', 'pinyin_name', 'English_name', 'latin_name']
        interfaces = (relay.Node, )

class PrescriptionNode(DjangoObjectType):
    herbs = DjangoFilterConnectionField(HerbNode)
    class Meta:
        model = models.Prescription
        filter_fields = ['chinese_name', 'english_name', 'pinyin_name']
        interfaces = (relay.Node, )

class KEGGPathwayNode(DjangoObjectType):
    class Meta:
        model = models.KEGGPathway
        filter_fields = ['kegg_id', 'name']
        interfaces = (relay.Node, )


class TargetNode(DjangoObjectType):
    compounds = DjangoFilterConnectionField(CompoundNode)
    class Meta:
        model = models.Target
        filter_fields = [
            'target_name',
            'gene_name',
            'uniprot_name'
        ]
        interfaces = (relay.Node, )

class Query(AbstractType):
    compound = relay.Node.Field(CompoundNode)
    all_compounds = DjangoFilterConnectionField(CompoundNode)

    herb = relay.Node.Field(HerbNode)
    all_herbs = DjangoFilterConnectionField(HerbNode)

    prescription = relay.Node.Field(PrescriptionNode)
    all_prescriptions = DjangoFilterConnectionField(PrescriptionNode)

    keggpathway = relay.Node.Field(KEGGPathwayNode)
    all_keggpathways = DjangoFilterConnectionField(KEGGPathwayNode)

    chembl = relay.Node.Field(ChEMBLNode)
    all_chembls = DjangoFilterConnectionField(ChEMBLNode)

    target = relay.Node.Field(TargetNode)
    all_targets = DjangoFilterConnectionField(TargetNode)




