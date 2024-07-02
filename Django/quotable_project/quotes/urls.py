from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.quote_list),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view()),
]
