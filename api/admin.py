from django.contrib import admin
from .models import Product, Collection, ShoppingCart, UserAddress

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(ShoppingCart)
admin.site.register(UserAddress)
