
from .Utils import fetch_by_id
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from ..models import Product, Collection
from .Types import ProductType, CollectionType


class Query(ObjectType):
    product = graphene.Field(ProductType, id=graphene.Int())
    collection = graphene.Field(CollectionType, id=graphene.Int())
    products = graphene.List(ProductType)
    collections = graphene.List(CollectionType)

    def resolve_product(self, info, **kwargs):
        return fetch_by_id(kwargs.get('id'), Product)

    def resolve_collection(self, info, **kwargs):
        return fetch_by_id(kwargs.get('id'), Collection)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_collections(self, info, **kwargs):
        return Collection.objects.all()
