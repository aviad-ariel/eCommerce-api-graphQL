from django.db import models

class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    description = models.TextField()
    supplier_name = models.CharField(max_length=50)
    is_published = models.BooleanField()
    selling_price = models.FloatField()
    buying_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name='collections')
    average_products_price = models.FloatField()

    def __str__(self):
        return self.name
