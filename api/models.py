from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
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

    def __str__(self):
        return self.name

class ShoppingCart(Collection):
    objects = models.Manager()
    user = models.OneToOneField(User, related_name='shoppingCart', on_delete=models.CASCADE)

    @classmethod
    @receiver(signals.post_save, sender=User)
    def create_shopping_cart(sender, instance, created, **kwargs):
        if created:
            return ShoppingCart(user=instance).save()
            
    def __str__(self):
        return str(self.user)


class UserAddress(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    country = models.TextField()
    state = models.TextField()
    city = models.TextField()
    street_name = models.TextField()

    def __str__(self):
        return str(self.user)
    



