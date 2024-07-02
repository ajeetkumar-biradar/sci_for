from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Product, Cart


# Define a new UserAdmin class
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_staff')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register other models
admin.site.register(Product)
admin.site.register(Cart)
