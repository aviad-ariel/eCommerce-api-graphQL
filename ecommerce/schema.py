import graphene
import api.graphql.Query as Queries
import api.graphql.Mutations.Mutation as Mutations


class Query(Queries.Query, graphene.ObjectType):
    pass


class Mutation(Mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
