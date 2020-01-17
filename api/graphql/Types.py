from ..models import Product, Collection
from graphene_django.types import DjangoObjectType, ObjectType


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CollectionType(DjangoObjectType):
    class Meta:
        model = Collection
