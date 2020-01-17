import graphene


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    supplier_name = graphene.String()
    is_published = graphene.Boolean()
    selling_price = graphene.Float()
    buying_price = graphene.Float()


class CollectionInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    products = graphene.List(ProductInput)
