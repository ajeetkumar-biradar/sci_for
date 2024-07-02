# portfolio/views.py
from django.shortcuts import render
from .models import UserProfile

def home(request):
    user_profile = UserProfile.objects.first()  # Assuming there's only one user profile
    return render(request, 'portfolio/home.html', {'user_profile': user_profile})
