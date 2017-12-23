import sys
import inspect

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework import viewsets, views
from .models import *   #NOQA
from .serializers import *  #NOQA
from rest_framework.response import Response
# Create your views here.

__all__ = []


def _generate_all():
    current_module = sys.modules[__name__]
    for name in dir(current_module):
        obj = getattr(current_module, name, None)
        if inspect.isclass(obj):
            if issubclass(obj, views.APIView) or issubclass(obj, viewsets.ViewSet):
                __all__.append(name)


"""Identity views grop"""


class ChineseIdentityViewSet(viewsets.ModelViewSet):
    queryset = ChineseIdentity.objects.all()
    serializer_class = ChineseIdentitySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class EnglishIdentityViewSet(viewsets.ModelViewSet):
    queryset = EnglishIdentity.objects.all()
    serializer_class = EnglishIdentitySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


""" compound views group """


class CompoundViewSet(viewsets.ModelViewSet):
    queryset = Compound.objects.all()
    serializer_class = CompoundSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
#
#
# class CompoundList(generics.ListCreateAPIView):
#     model = Compound
#     queryset = Compound.objects.all()
#     serializer_class = CompoundSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]
#
#
# class CompoundDetail(generics.RetrieveUpdateDestroyAPIView):
#     model = Compound
#     queryset = Compound.objects.all()
#     serializer_class = CompoundSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]

"""Structure views group"""


# class StructureViewSet(viewsets.ModelViewSet):
#     queryset = Structure.objects.all()
#     serializer_class = StructureSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]


# class StructureList(generics.ListCreateAPIView):
#     model = Structure
#     queryset = Structure.objects.all()
#     serializer_class = StructureSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]
#
#
# class StructureDetail(generics.RetrieveUpdateDestroyAPIView):
#     model = Structure
#     queryset = Structure.objects.all()
#     serializer_class = StructureSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]


"""Herb views group"""


class HerbViewSet(viewsets.ModelViewSet):
    queryset = Herb.objects.all()
    serializer_class = HerbSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
#
# class HerbList(generics.ListCreateAPIView):
#     model = Herb
#     queryset = Herb.objects.all()
#     serializer_class = HerbSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]
#
#
# class HerbDetail(generics.RetrieveUpdateDestroyAPIView):
#     model = Herb
#     queryset = Herb.objects.all()
#     serializer_class = HerbSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]


# CID view set
class CIDViewSet(viewsets.ModelViewSet):
    queryset = CID.objects.all()
    serializer_class = CIDSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


# CAS view set
class CASViewSet(viewsets.ModelViewSet):
    queryset = CAS.objects.all()
    serializer_class = CASSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


# class ChEMBLViewSet(viewsets.ModelViewSet):
#     queryset = ChEMBL.objects.all()
#     serializer_class = ChEMBlSerializer
#     permission_classes = [
#         permissions.DjangoModelPermissionsOrAnonReadOnly
#     ]


class TCMTaxonomyViewSet(viewsets.ModelViewSet):

    # def list(self, request, *args, **kwargs):
    #     tree = TCMTaxonomy.objects.all()
    #     page = self.paginate_queryset(tree)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = TCMTaxonomy.objects.all()
    #     taxonomy = get_object_or_404(queryset, pk=pk)
    #     serializer = TCMTaxonomySerializer(taxonomy)
    #     return Response(serializer.data)

    queryset = TCMTaxonomy.objects.all()
    serializer_class = TCMTaxonomySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class KEGGPathwayViewSet(viewsets.ModelViewSet):
    queryset = KEGGPathway.objects.all()
    serializer_class = KEGGPathwaySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class KEGGPathwayCategoryViewSet(viewsets.ModelViewSet):
    queryset = KEGGPathwayCategory.objects.all()
    serializer_class = KEGGPathwayCategorySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class KEGGSimilarityViewSet(viewsets.ModelViewSet):
    queryset = KEGGSimilarity.objects.all()
    serializer_class = KEGGSimilaritySerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class KEGGCompoundViewSet(viewsets.ModelViewSet):
    queryset = KEGGCompound.objects.all()
    serializer_class = KEGGCompoundSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


_generate_all()