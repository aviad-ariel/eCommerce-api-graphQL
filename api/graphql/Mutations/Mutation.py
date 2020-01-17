import graphene
from .ProductMutations import CreateProduct, UpdateProduct


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
