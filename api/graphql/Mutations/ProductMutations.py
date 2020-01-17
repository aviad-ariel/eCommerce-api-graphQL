from ..Inputs import ProductInput, CollectionInput
from ..Types import ProductType, CollectionType
from ...models import Product, Collection
from ..Utils import input_to_product
import graphene


class CreateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput()

    ok = graphene.Boolean()
    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, input=None):
        product = input_to_product(input, Product)
        product.save()
        return CreateProduct(ok=True, product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        input = ProductInput()

    ok = graphene.Boolean()
    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        product = Product.objects.get(pk=id)
        if product:
            ok = True
            for key in input:
                setattr(product, key, input[key])
            product.save()
            return UpdateProduct(ok=ok, product=product)
        return UpdateProduct(ok=ok, product=None)
