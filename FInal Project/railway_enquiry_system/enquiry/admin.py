from django.contrib import admin
from .models import Train, Booking, Profile  # Make sure to import Profile
from django.utils.html import format_html


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        'train_number', 'name', 'source', 'destination',
        'departure_time', 'arrival_time', 'total_seats', 'available_seats',
        'sleeper_price', 'first_class_price', 'second_class_price', 'first_tier_price'
    )
    search_fields = ('train_number', 'name', 'source', 'destination')
    list_filter = ('source', 'destination')
    ordering = ('departure_time',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'train', 'seat_number', 'passenger_name', 'email',
        'booking_date', 'is_cancelled'
    )
    search_fields = ('train__name', 'seat_number', 'passenger_name', 'email')
    list_filter = ('train', 'booking_date', 'is_cancelled')
    ordering = ('-booking_date',)


from django.contrib import admin
from django.utils.html import format_html
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag')
    search_fields = ('user__username',)
    list_filter = ('user__is_active',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="border-radius: 50%; width: 50px; height: 50px;" />'.format(obj.image.url))
        return format_html('<span style="color:red;">No Image</span>')

    image_tag.short_description = 'Profile Image'
