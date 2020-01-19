from ...models import Collection, Product
from ..Types import CollectionType, ProductType
from ..Inputs import CollectionInput, ProductInput
import graphene


class CreateCollection(graphene.Mutation):
    class Arguments:
        input = CollectionInput()

    ok = graphene.Boolean()
    collection = graphene.Field(CollectionType)
    not_found = graphene.List(graphene.Int)
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        products = []
        if input.products:
            not_found = []
            for product in input.products:
                try:
                    product_instance = Product.objects.get(pk=product.id)
                    products.append(product_instance)
                except:
                    not_found.append(product.id)
        collection = Collection(name=input.name)
        collection.save()
        collection.products.set(products)
        return CreateCollection(ok=ok, collection=collection, not_found=not_found)

# updates the products field on given collection.
# in order to add product provide collection id and product id,
# to remove product set remove argument to true.
class UpdateCollectionProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        input = ProductInput()
        remove = graphene.Boolean()

    ok = graphene.Boolean()
    collection = graphene.Field(CollectionType)

    @staticmethod
    def mutate(root, info, id, input, **kwargs):
        ok = False
        collection = Collection.objects.get(pk=id)
        if collection:
            ok = True
            collection.products.remove(input.id) if kwargs.get(
                'remove') else collection.products.add(input.id)
            collection.save()
            return UpdateCollectionProduct(ok=ok, collection=collection)
        return UpdateCollectionProduct(ok=ok, collection=None)
