from django.contrib import admin
from .models import Coffe


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


admin.site.register(Coffe, CoffeeAdmin)
