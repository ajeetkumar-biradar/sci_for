from django.contrib import admin
from .models import Product, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'total_quantity')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('name',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'product')

admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
