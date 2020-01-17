import graphene
import api.graphql.Query as graphql

class Query(graphql.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)