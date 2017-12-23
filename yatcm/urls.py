"""yatcm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework_swagger.views import get_swagger_view
from .views import IndexView, AboutView, ContactView
from graphene_django.views import GraphQLView

schema_view = get_swagger_view(title="yatcm API")

urlpatterns = [
    url(r"^yatcm/$", IndexView.as_view(), name="index"),
    url(r'yatcm/about/$', AboutView.as_view(), name="about"),
    url(r'yatcm/contact/$', ContactView.as_view(), name="contact"),
    url(r'^yatcm/admin/', admin.site.urls),
    url(r'^yatcm/graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)), name="graphql"),
    url(r"^yatcm/", include('compounds.urls')),
    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'yatcm/api-auth', include("rest_framework.urls", namespace='rest_framework')),
    url(r"^yatcm/docs/$", schema_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)