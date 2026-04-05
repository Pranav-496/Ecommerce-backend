from django.contrib import admin

from store.models import Cart, CartItem, Category, Order, OrderItem, Product, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)  