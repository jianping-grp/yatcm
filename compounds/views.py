# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from collections import defaultdict
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import StreamingHttpResponse
from django.core import serializers
from .models import *    #NOQA
from django.views.generic import TemplateView, DetailView, View, ListView
from django_rdkit.config import config
from django_rdkit.models import *
from rdkit import Chem
from itertools import chain
from django.template import loader
# Create your views here.


# __all__ = [
#     "SearchView",
#     "StructureSearchView",
#     "IdentifySearchView",
#     "CompoundRelatedCompoundsListView",
#     "CompoundDetailView",
#     "CompoundRelatedHerbsListView",
#     "HerbDetailView",
#     'HerbRelatedCompoundsView',
#     "HerbRelatedPrescriptionView",
#     "PrescriptionDetailView",
# ]


class SearchView(TemplateView):
    template_name = "search.html"

class BrowseView(TemplateView):
    template_name = 'browse.html'

class StructureSearchView(View):

    def post(self, request):
        if request.is_ajax():
            data = request.POST
            is_sub = data.get("is_sub")
            tanimoto = float(data.get("tanimoto", 0.8))
            smiles = data.get("smiles")
            try:
                smiles = Chem.CanonSmiles(smiles)
            except:
                return "Sorry, the structure is not appropriate!"
            if is_sub and smiles:
                compounds = self._substructure_search(smiles)
                paginator = Paginator(compounds, 10)

                ## My paginator code ###
                try:
                    paginator_compounds = paginator.page(1)
                except PageNotAnInteger:
                    paginator_compounds = paginator.page(1)
                except EmptyPage:
                    paginator_compounds = paginator.page(paginator.num_pages)

                respone = render(
                    request, template_name="result/compounds_result.html",
                    context={
                        "compounds": paginator_compounds,
                             }
                )
                return StreamingHttpResponse(respone.content)

            elif not is_sub and smiles:
                compounds = self._similarity_search(smiles, tanimoto=tanimoto)
                paginator = Paginator(compounds, 10)

                try:
                    paginator_compounds = paginator.page(1)
                except PageNotAnInteger:
                    paginator_compounds = paginator.page(1)
                except EmptyPage:
                    paginator_compounds = paginator.page(paginator.num_pages)

                response = render(
                    request,
                    template_name="result/compounds_result.html",
                    context={
                        "compounds": paginator_compounds,
                    }
                )
                return StreamingHttpResponse(response.content)

    @staticmethod
    def _similarity_search(smiles, tanimoto=0.8):
        config.tanimoto_threshold = tanimoto
        value = MORGANBV_FP(Value(smiles))
        compound_list = Compound.objects.filter(
            bfp__tanimoto=value
        )
        return compound_list

    @staticmethod
    def _substructure_search(smiles):
        compound_list = Compound.objects.filter(mol__hassubstruct=QMOL(Value(smiles)))
        # print compound_list
        return compound_list

class IdentifySearchView(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
            type = data.get("type").strip().lower()
            query = data.get("query").strip().lower()
            context = defaultdict()
            if type == "compound" or type == "formula":
                compounds = self._compound_search(query)
                context.setdefault('compounds', compounds)
            elif type == 'cid':
                compounds = self._cid_search(query)
                context.setdefault('compounds', compounds)
            elif type == 'cas':
                compounds = self._cas_search(query)
                context.setdefault('compounds', compounds)
            elif type == "herb":
                herbs = self._herb_search(query)
                context.setdefault("herbs", herbs)
            elif type == "prescription":
                prescriptions = self._prescription_search(query)
                context.setdefault("prescriptions", prescriptions)
            elif type == "formula":
                compounds = self._formula_search(query)
                context.setdefault("compounds", compounds)
            elif type == "all":
                compounds = self._compound_search(query)
                herbs = self._herb_search(query)
                prescriptions = self._prescription_search(query)
                context.setdefault('compounds', compounds)
                context.setdefault("herbs", herbs)
                context.setdefault("prescriptions", prescriptions)
            return StreamingHttpResponse(render(request, template_name="result/result.html", context=context))

    @staticmethod
    def _compound_search(query):
        compound_list = Compound.objects.filter(
            Q(english_name__icontains=query) |
            Q(chinese_name__icontains=query) |
            Q(formula__iexact=query) |
            Q(englishidentity__identity__icontains=query) |
            Q(chineseidentity__identity__icontains=query)
        )
        return compound_list.distinct()

    # @staticmethod
    # def _compound_search(query):
    #     compound_list = Compound.objects.filter(
    #         Q(english_name__icontains=query) |
    #         Q(chinese_name__icontains=query) |
    #         Q(formula__iexact=query) |
    #         Q(englishidentity__identity__icontains=query) |
    #         Q(chineseidentity__identity__icontains=query) |
    #         Q(chineseidentity__pinyin_name__icontains=query)
    #     )
    #     return compound_list.distinct()

    @staticmethod
    def _herb_search(query):
        herb_list = Herb.objects.filter(
            Q(English_name__icontains=query) |
            Q(Chinese_name__icontains=query) |
            Q(pinyin_name__icontains=query)
        )
        return herb_list


    @staticmethod
    def _formula_search(query):
        compound_list = Compound.objects.filter(
            formula__iexact=query
        )
        return compound_list

    @staticmethod
    def _prescription_search(query):
        prescription_list = Prescription.objects.filter(
            Q(chinese_name__icontains=query) |
            Q(english_name__icontains=query) |
            Q(pinyin_name__icontains=query)
        )
        return prescription_list
    @staticmethod
    def _cid_search(query):
        try:
            query = int(query)
            compound_list = Compound.objects.filter(
                cid__cid=query
            ).distinct()
        except ValueError:
            compound_list = Compound.objects.none()
        return compound_list

    @staticmethod
    def _cas_search(query):
        compound_list = Compound.objects.filter(
            cas__cas=query
        ).distinct()
        return compound_list


# detail pages and list pages
class CompoundDetailView(DetailView):
    model = Compound
    template_name = "compound_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CompoundDetailView, self).get_context_data()
        compound = self.get_object()

        # related_chembl_compounds = compound.chembls.all()
        chembls = compound.chembls.filter(same_or_similar='same')
        related_chembls = compound.chembls.filter(same_or_similar='similar')
        related_herbs = compound.herb_set.all()
        related_tcmdid_herbs = compound.tcmid_herbs_set.all()
        related_targets = compound.target_set.all()

        related_first_catagory = compound.compoundfirstcatagory_set.all()
        related_second_catagory = compound.compoundsecondcatagory_set.all()

        # context['related_chembl_compounds'] = related_chembl_compounds
        context['chembls'] = chembls
        context['related_chembls'] = related_chembls
        context['related_herbs'] = related_herbs
        context['related_tcmid_herbs'] = related_tcmdid_herbs
        context['related_targets'] = related_targets
        context['related_first_catagory'] = related_first_catagory
        context['related_second_catagory'] = related_second_catagory
        return context


class CompoundRelatedCompoundsListView(TemplateView):
    template_name = "compound_list.html"

    def get_context_data(self, **kwargs):
        context = super(CompoundRelatedCompoundsListView, self).get_context_data()
        pk = int(kwargs['pk'])
        compound = Compound.objects.get(pk=pk)
        related_compounds = compound.related_compounds.all()
        context['compounds'] = related_compounds
        return context

### New Code###
class CompoundRelatedChemblListView(TemplateView):
    template_name = 'related_chembl_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompoundRelatedChemblListView, self).get_context_data()
        pk = int(kwargs['pk'])
        compound = Compound.objects.get(pk=pk)
        related_chembls = compound.chembls.filter(same_or_similar='similar')
        context['related_chembls'] = related_chembls
        return context

class ChemblAssayListView(TemplateView):
    template_name = 'chembl_assay_list.html'


class CompoundRelatedHerbsListView(TemplateView):
    template_name = 'herb_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompoundRelatedHerbsListView, self).get_context_data()
        pk = int(kwargs['pk'])
        compound = Compound.objects.get(pk=pk)
        related_herbs = compound.herb_set.all()
        context['herbs'] = related_herbs
        return context

class CompoundRelatedTcmidHerbListView(TemplateView):
    template_name = 'tcmid_herb_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompoundRelatedTcmidHerbListView, self).get_context_data()
        pk = int(kwargs['pk'])
        compound = Compound.objects.get(pk=pk)
        related_tcmid_herbs = compound.tcmid_herbs_set.all()
        context['tcmid_herbs'] = related_tcmid_herbs
        return context

class CompoundRelatedTargetsListView(TemplateView):
    template_name = 'target_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompoundRelatedTargetsListView, self).get_context_data()
        pk = int(kwargs['pk'])
        compound = Compound.objects.get(pk=pk)
        related_targets = compound.target_set.all()
        context['related_targets'] = related_targets
        return context

class HerbDetailView(DetailView):
    template_name = "herb_detail.html"
    model = Herb

    def get_context_data(self, **kwargs):
        context = super(HerbDetailView, self).get_context_data()
        herb = self.get_object()
        taxonomy = herb.taxonomy

        if taxonomy:
            taxonomy_list = taxonomy.get_ancestors(include_self=True)
            context['taxonomy_list'] = taxonomy_list

        if herb.effect:
            tcmid_url = 'http://www.megabionet.org/tcmid/herbsearch/?chinese_Name=' + '+'.join(herb.pinyin_name.split()) + '&english_Name='
            context['tcmid_url'] = tcmid_url

        related_herb_id = herb.related_herbs_id
        related_herbs = Herb.objects.filter(related_herbs_id=related_herb_id).distinct()
        # print type(related_herbs)
        context['herbs'] = related_herbs
        compounds = herb.compounds.all()
        # print len(compounds)
        context['compounds'] = compounds
        if len(compounds) > 20:
            context['compounds_1_10'] = compounds[:10]
            context['compounds_10_20'] = compounds[10:20]
            context['compounds_20_last'] = compounds[20:]
        else:
            if len(compounds) % 2 == 0:
                idx = len(compounds) / 2
                context['compounds_previous'] = compounds[:idx]
                context['compounds_last'] = compounds[idx:]
            else:
                idx = len(compounds) / 2 + 1
                context['compounds_previous'] = compounds[:idx]
                context['compounds_last'] = compounds[idx:]
        return context

class HerbRelatedHerbsView(TemplateView):
    template_name = 'herb_list.html'

    def get_context_data(self, **kwargs):
        context = super(HerbRelatedHerbsView, self).get_context_data()
        pk = int(kwargs['pk'])
        herb = Herb.objects.get(pk=pk)
        related_herbs = Herb.objects.filter(related_herbs_id=herb.related_herbs_id).distinct()
        context['herbs'] = related_herbs
        return context

class HerbRelatedCompoundsView(TemplateView):
    template_name = 'compound_list.html'

    def get_context_data(self, **kwargs):
        context = super(HerbRelatedCompoundsView, self).get_context_data()
        pk = kwargs['pk']
        herb = Herb.objects.get(pk=pk)
        related_compounds = herb.compounds.all()
        context['compounds'] = related_compounds
        return context


class HerbRelatedPrescriptionView(TemplateView):
    template_name = "prescription_list.html"

    def get_context_data(self, **kwargs):
        context = super(HerbRelatedPrescriptionView, self).get_context_data()
        pk = kwargs['pk']
        herb = Herb.objects.get(pk=pk)
        related_prescriptions = herb.prescription_set.all()
        context['prescriptions'] = related_prescriptions
        return context


class PrescriptionDetailView(DetailView):
    template_name = "prescription_detail.html"
    model = Prescription

    def get_context_data(self, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data()
        prescription = self.get_object()
        herbs = prescription.herbs.all()

        compounds = herbs[0].compounds.all()
        for herb in herbs[1:]:
            compounds = chain(compounds, herb.compounds.all())
        context['compounds'] = list(compounds)
        context['compounds_top10'] = list(compounds)[:10]
        context['compounds_10_last'] = list(compounds)[10:]
        return context


class HerbListView(ListView):
    model = Herb

class HerbsBrowseListView(ListView):
    model = Herb
    context_object_name = 'herb_list'
    template_name = 'herbs_browse_list_view.html'
    paginate_by = 20

class PrescriptionBrowseListView(ListView):
    model = Prescription
    context_object_name = 'prescription_list'
    template_name = 'prescriptions_browse_list_view.html'
    paginate_by = 20

class PathwayDetailView(DetailView):
    model = KEGGPathway
    context_object_name = 'keggpathway'
    template_name = 'pathway_detail.html'

class PathwaysBrowseListView(ListView):
    model = KEGGPathway
    context_object_name = 'pathway_list'
    template_name = 'pathways_browse_list_view.html'
    paginate_by = 20

def compound_pathway_mapping_view(request, cpd_id, kegg_pathway_id):
    template = loader.get_template('kegg_pathway.html')
    pathway = KEGGPathway.objects.get(kegg_id=kegg_pathway_id)
    cpd = Compound.objects.get(id=cpd_id)
    kegg_cpd_id_list = [x.kegg_id for x in cpd.keggcompound_set.all()]
    mapping_kegg_cpds = pathway.kgml_parser(kegg_cpd_id_list)
    context = {
        'mapping_kegg_cpds': mapping_kegg_cpds,
        'pathway': pathway,
        'tcm_cpd': cpd
    }
    return HttpResponse(template.render(context, request))
