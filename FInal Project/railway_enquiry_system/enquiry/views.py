from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Train, Booking
from .forms import BookingForm, UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

def index(request):
    trains = Train.objects.all()
    return render(request, 'enquiry/index.html', {'trains': trains})

def search_trains(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        trains = Train.objects.filter(source=source, destination=destination)
        return render(request, 'enquiry/train_list.html', {'trains': trains})
    return render(request, 'enquiry/search_trains.html')

def check_seat_availability(request, train_id):
    train = get_object_or_404(Train, id=train_id)
    bookings = Booking.objects.filter(train=train)
    return render(request, 'enquiry/seat_availability.html', {'train': train, 'bookings': bookings})

@login_required
def book_ticket(request, train_id):
    train = get_object_or_404(Train, id=train_id)
    ticket_prices = {
        'SL': float(train.sleeper_price),
        'FC': float(train.first_class_price),
        'SC': float(train.second_class_price),
        '1T': float(train.first_tier_price),
    }
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Assign seat number
            booking.train = train
            booking.seat_number = train.total_seats - train.available_seats + 1
            if train.available_seats > 0:
                train.available_seats -= 1
                train.save()
                booking.save()
                messages.success(request, 'Booking successful!')
                return redirect('booking_confirmation', booking_id=booking.id)
            else:
                messages.error(request, 'No available seats')
    else:
        form = BookingForm()
    return render(request, 'enquiry/book_ticket.html', {'form': form, 'train': train, 'ticket_prices': ticket_prices})


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'enquiry/booking_confirmation.html', {'booking': booking})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        train = booking.train
        train.available_seats += 1
        train.save()
        booking.delete()
        return redirect('cancellation_confirmation', booking_id=booking_id)
    return render(request, 'enquiry/cancel_booking.html', {'booking': booking})

def cancellation_confirmation(request, booking_id):
    return render(request, 'enquiry/cancellation_confirmation.html', {'booking_id': booking_id})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.FILES.get('image')

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        profile = Profile.objects.create(user=user)
        if image:
            profile.image = image
            profile.save()

        login(request, user)
        messages.success(request, 'Your account has been created successfully!')
        return redirect('index')

    return render(request, 'enquiry/register.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'enquiry/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def booked_tickets(request):
    bookings = Booking.objects.filter(is_cancelled=False)
    return render(request, 'enquiry/booked_tickets.html', {'bookings': bookings})

@login_required
def train_portfolio(request):
    return render(request, 'enquiry/train_portfolio.html')

@login_required
def profile(request):
    user = request.user  # Get the current logged-in user
    context = {
        'user': user
    }
    return render(request, 'enquiry/profile.html', context)
