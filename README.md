# eCommerce-api-graphQL
GraphQL API built with Django(using [graphene-django](https://github.com/graphql-python/graphene-django))

### Queries:
* product(id: Int): ProductType| fetch Product by id
* collection(id: Int): CollectionType| fetch Collection by id
* products: [ProductType]| fetch all Products
* collections: [CollectionType]| fetch all Collections
* user(id: Int): UserType| fetch user by id
* orderCheckout(id: Int): Float| fetch user shopping cart sum

### Mutations:
* createProduct(input: ProductInput): CreateProduct
* updateProduct(id: Int input: ProductInput): UpdateProduct
* createCollection(input: CollectionInput): CreateCollection
* updateCollectionProduct(
    id: Int
    input: ProductInput
    remove: Boolean
  ): UpdateCollectionProduct
* updateShoppingcart(
    id: Int
    input: ProductInput
    remove: Boolean
  ): UpdateShoppingCart
* registerUser(
    email: String
    password: String
    username: String
  ): RegisterUser
* createUserAddress(input: UserAddressInput): CreateUserAddress
* tokenAuth(username: String!password: String!): ObtainJSONWebToken| [django-graphql-jwt](https://django-graphql-jwt.domake.io/) mutation
* verifyToken(token: String!): Verify| [django-graphql-jwt](https://django-graphql-jwt.domake.io/) mutation
* refreshToken(token: String!): Refresh| [django-graphql-jwt](https://django-graphql-jwt.domake.io/) mutation

#### usage:
    pip install
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
