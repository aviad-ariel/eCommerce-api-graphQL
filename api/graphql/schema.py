import graphene
from .Query import Query
from .Mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
