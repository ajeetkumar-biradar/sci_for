from django.urls import path
from . import views
from .views import booked_tickets

urlpatterns = [
    path('', views.index, name='index'),
    path('search_trains/', views.search_trains, name='search_trains'),
    path('check_seat_availability/<int:train_id>/', views.check_seat_availability, name='check_seat_availability'),
    path('book_ticket/<int:train_id>/', views.book_ticket, name='book_ticket'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('cancellation_confirmation/<int:booking_id>/', views.cancellation_confirmation, name='cancellation_confirmation'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('booked_tickets/', booked_tickets, name='booked_tickets'),
    path('train-portfolio/', views.train_portfolio, name='train_portfolio'),
    path('profile/', views.profile, name='profile'),
]

