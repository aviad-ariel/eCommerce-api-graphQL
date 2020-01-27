from graphql import GraphQLError

def fetch_by_id(query, model):
    try:
        fetched_data = model.objects.get(pk=query)
    except model.DoesNotExist:
        fetched_data = None
    return fetched_data


def input_to_product(input, Model):
    return Model(name=input.name, description=input.description, supplier_name=input.supplier_name,
                   is_published=input.is_published, selling_price=input.selling_price, buying_price=input.buying_price)

def query_premission(function):
    def wrapper(self, info, **kwargs):
        return function(self, info, **kwargs) if kwargs.get('id') == info.context.user.id else GraphQLError("You can't access that :(")
    return wrapper

def mutation_premission(function):
    def wrapper(cls, root, info, **kwargs):
        print(kwargs.get('id'), info.context.user)
        return function(cls, root, info, **kwargs) if info.context.user.id==kwargs.get('id') else GraphQLError("You can't access that :(")
    return wrapper