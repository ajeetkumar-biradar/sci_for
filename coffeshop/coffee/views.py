from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffe


def home(request):
    coffee = Coffe.objects.all()
    return render(request, 'home.html', {'coffee': coffee})
