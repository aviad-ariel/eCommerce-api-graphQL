
from ..models import Product


def fetch_by_id(query, model):
    try:
        fetched_data = model.objects.get(pk=query)
    except model.DoesNotExist:
        fetched_data = None
    return fetched_data


def input_to_product(input, Model):
    return Product(name=input.name, description=input.description, supplier_name=input.supplier_name,
                   is_published=input.is_published, selling_price=input.selling_price, buying_price=input.buying_price)
