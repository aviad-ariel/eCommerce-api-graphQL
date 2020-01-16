def fetch(query, model):
    try:
        fetched_data = model.objects.get(pk=query)
    except model.DoesNotExist:
        fetched_data = None
    return fetched_data

def average():
    pass