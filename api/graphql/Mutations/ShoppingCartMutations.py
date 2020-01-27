import graphene
from ...models import ShoppingCart, User
from ..Types import ShoppingCartType, CollectionType
from ..Inputs import ProductInput
from .CollectionMutations import UpdateCollectionProduct, CreateCollection
from graphql_jwt.decorators import login_required, user_passes_test
from ..Utils import mutation_premission


class UpdateShoppingCart(UpdateCollectionProduct):
    class Arguments:
        id = graphene.Int()
        input = ProductInput()
        remove = graphene.Boolean()
    ok = graphene.Boolean()
    collection = graphene.Field(CollectionType)

    @classmethod
    @mutation_premission
    @login_required
    def mutate(cls, root, info, input, **kwargs):
        print(info.context.user)
        user_cart = User.objects.get(pk=kwargs.get('id')).shoppingCart.id
        return super().mutate(root, info, input, id=user_cart)



