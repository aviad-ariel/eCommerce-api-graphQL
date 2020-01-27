from ..models import Product, Collection, ShoppingCart, UserAddress
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CollectionType(DjangoObjectType):
    class Meta:
        model = Collection


class ShoppingCartType(DjangoObjectType):
    class Meta:
        model = ShoppingCart


class UserAddressType(DjangoObjectType):

    class Meta:
        model = UserAddress