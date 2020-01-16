import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Product, Collection
from .Utils import fetch


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CollectionType(DjangoObjectType):
    class Meta:
        model = Collection


class Query(ObjectType):
    product = graphene.Field(ProductType, id=graphene.Int())
    collection = graphene.Field(CollectionType, id=graphene.Int())
    products = graphene.List(ProductType)
    collections = graphene.List(CollectionType)

    def resolve_product(self, info, **kwargs):
        return fetch(kwargs.get('id'), Product)

    def resolve_collection(self, info, **kwargs):
        return fetch(kwargs.get('id'), Collection)

    def resolve_products(self, info, **kwargs):
        print("in fetch")
        return Product.objects.all()

    def resolve_collections(self, info, **kwargs):
        return Collection.objects.all()

schema = graphene.Schema(query=Query)