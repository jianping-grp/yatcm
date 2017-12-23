from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .api import *  # NOQA
from .views import *  # NOQA

router = DefaultRouter()
router.register(r"identity/en", EnglishIdentityViewSet)
router.register(r"identity/ch", ChineseIdentityViewSet)
router.register(r'compounds', CompoundViewSet)
# router.register(r'structures', StructureViewSet)
router.register(r'herbs', HerbViewSet)
router.register(r'cids', CIDViewSet)
router.register(r'cass', CASViewSet)
# router.register(r'chembls', ChEMBLViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'keggcompounds', KEGGCompoundViewSet)
router.register(r'keggpathways', KEGGPathwayViewSet)
router.register(r'keggpathwaycategories', KEGGPathwayCategoryViewSet)
router.register(r'keggsimilarities', KEGGSimilarityViewSet)
router.register(r'taxonomies', TCMTaxonomyViewSet)
apiurls = router.urls

compounds_urls = [
    url(r"^(?P<pk>\d+)/detail/$", CompoundDetailView.as_view(), name="compound_detail"),
    url(
        r"^(?P<pk>\d+)/related-compounds$",
        CompoundRelatedCompoundsListView.as_view(),
        name="compound_related_compounds"
    ),
    url(
        r'^(?P<pk>\d+)/related-herbs$',
        CompoundRelatedHerbsListView.as_view(),
        name="compound_related_herbs"
    ),
    url(
        r'^(?P<pk>\d+)/relate-tcmid-herbs$',
        CompoundRelatedTcmidHerbListView.as_view(),
        name='compound_related_tcmid_herbs'
    ),
    url(
        r'^(?P<pk>\d+)/related-chembl-compounds$',
        CompoundRelatedChemblListView.as_view(),
        name='compound_related_chembl_compounds'
    ),
    url(
        r'^(?P<pk>\d+)/related-chembl-assays$',
        ChemblAssayListView.as_view(),
        name='compound_related_chembl_assays'
    ),
    url(
        r'^(?P<pk>\d+)/related-targets$',
        CompoundRelatedTargetsListView.as_view(),
        name='compound_related_targets'
    ),
]

herb_urls = [
    url(r'^(?P<pk>\d+)/detail/$', HerbDetailView.as_view(), name="herb_detail"),
    url(
        r'^(?P<pk>\d+)/related-compounds$',
        HerbRelatedCompoundsView.as_view(),
        name='herb_related_compounds'
        ),
    url(r'^(?P<pk>\d+)/related-herbs$',
        HerbRelatedHerbsView.as_view(),
        name='herb_related_herbs'),
    url(
        r'^(?P<pk>\d+)/related-prescription$',
        HerbRelatedPrescriptionView.as_view(),
        name='herb_related_prescription'
        ),

]


prescription_urls = [
    url(r'^(?P<pk>\d+)/detail/$', PrescriptionDetailView.as_view(), name='prescription_detail'),
]

search_url = [
    url(r'^$', SearchView.as_view(), name='search'),

    url(r'^structure/$', StructureSearchView.as_view(), name='structure-search'),
    url(r'^identify/$', IdentifySearchView.as_view(), name='identify-search'),
]

browse_urls = [
    url(r'^$', BrowseView.as_view(), name='browse'),
    url(r'^browse-herbs', HerbsBrowseListView.as_view(), name='browse-herbs'),
    url(r'^browse-prescriptions', PrescriptionBrowseListView.as_view(), name='browse-prescriptions'),
    url(r'^browse-pathways', PathwaysBrowseListView.as_view(), name='browse-pathways')
]

pathway_urls = [
    url(r'^(?P<pk>\d+)/detail/$', PathwayDetailView.as_view(), name='pathway_detail'),
]

# url config
urlpatterns = [
    url(r"^api/", include(apiurls)),

    url(r'^search/', include(search_url)),
    # compounds
    url(r"compounds/", include(compounds_urls)),

    # herbs
    url(r"^herbs/", include(herb_urls)),

    # prescription
    url(r'^prescription/', include(prescription_urls)),

    url(r'^browse/', include(browse_urls)),

    ###kegg pathway
    url(
        r'tcm-pathway/(?P<cpd_id>\d+)/(?P<kegg_pathway_id>\w+)',
        compound_pathway_mapping_view,
        name='compound_pathway_mapping_view'
    ),

    url(r'^pathway/', include(pathway_urls)),
]



