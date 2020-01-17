import graphene
from .Query import Query


schema = graphene.Schema(query=Query)
