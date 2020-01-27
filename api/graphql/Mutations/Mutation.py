import graphene
import graphql_jwt
from .ProductMutations import CreateProduct, UpdateProduct
from .CollectionMutations import CreateCollection, UpdateCollectionProduct
from .UserMutations import RegisterUser, CreateUserAddress
from .ShoppingCartMutations import UpdateShoppingCart

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    create_collection = CreateCollection.Field()
    update_collection_product = UpdateCollectionProduct.Field()
    update_shoppingCart = UpdateShoppingCart.Field()
    register_user = RegisterUser.Field()
    create_user_address = CreateUserAddress().Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()