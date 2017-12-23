import graphene
import compounds.schema
from graphene_django.debug import DjangoDebug

class Query(compounds.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(query=Query)
