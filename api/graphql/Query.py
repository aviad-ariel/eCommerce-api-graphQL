
from .Utils import fetch_by_id, query_premission
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from ..models import Product, Collection, User, ShoppingCart
from .Types import ProductType, CollectionType, UserType, ShoppingCartType
from graphql_jwt.decorators import login_required, user_passes_test
from django.db.models import Sum


class Query(ObjectType):
    product = graphene.Field(
        ProductType, id=graphene.Int())
    collection = graphene.Field(CollectionType, id=graphene.Int())
    products = graphene.List(ProductType)
    collections = graphene.List(CollectionType)
    user = graphene.Field(UserType, id=graphene.Int())
    order_checkout = graphene.Field(
        graphene.Float, id=graphene.Int())

    def resolve_product(self, info, **kwargs):
        return fetch_by_id(kwargs.get('id'), Product)

    def resolve_collection(self, info, **kwargs):
        return fetch_by_id(kwargs.get('id'), Collection)

    @login_required
    @query_premission
    def resolve_user(self, info, **kwargs):
        return fetch_by_id(kwargs.get('id'), User)

    @login_required
    @user_passes_test(lambda user: user.is_superuser)
    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    @login_required
    @user_passes_test(lambda user: user.is_superuser)
    def resolve_collections(self, info, **kwargs):
        return Collection.objects.all()

    @login_required
    @query_premission
    def resolve_order_checkout(self, info, **kwargs):
        user = User.objects.get(pk=kwargs.get('id'))
        return user.shoppingCart.products.aggregate(Sum('selling_price'))['selling_price__sum']
