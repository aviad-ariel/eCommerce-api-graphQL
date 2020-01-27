import graphene
from django.contrib.auth.models import User
from ..Types import UserType, ShoppingCartType, UserAddressType
from ...models import ShoppingCart, UserAddress
from ..Inputs import UserAddressInput
from graphql_jwt.decorators import login_required
from ..Utils import mutation_premission

class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(UserType)
    @staticmethod
    def mutate(root, info, username, email, password):
        user = User.objects.create_user(username, email, password)
        return RegisterUser(ok=True, user=user)


class CreateUserAddress(graphene.Mutation):
    class Arguments:
        input = UserAddressInput()

    ok = graphene.Boolean()
    address = graphene.Field(UserAddressType)

    @classmethod
    @login_required
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(pk=info.context.user.id)
        address = UserAddress(country=kwargs.get('input').country, state=kwargs.get(
            'input').state, city=kwargs.get('input').city, street_name=kwargs.get('input').street_name, user=user)
        print(address, user)
        address.save()
        return CreateUserAddress(ok=True, address=address)
