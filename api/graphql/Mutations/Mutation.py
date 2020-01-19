import graphene
from .ProductMutations import CreateProduct, UpdateProduct
from .CollectionMutations import CreateCollection, UpdateCollectionProduct


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    create_collection = CreateCollection.Field()
    update_collection_product = UpdateCollectionProduct.Field()