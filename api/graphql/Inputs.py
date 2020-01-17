import graphene

class productInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    supplier_name = graphene.String()
    is_published = graphene.Boolean()
    selling_price = graphene.Float()
    buying_price = graphene.Float()


class collectionInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    products = graphene.List(productInput)
