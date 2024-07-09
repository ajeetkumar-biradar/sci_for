# forms.py
from django import forms
from .models import Booking, Profile  # Ensure to import the Profile model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Booking, Profile, Train  # Import Train here



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'email']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.create(user=user)
            if self.cleaned_data['image']:
                profile.image = self.cleaned_data['image']
                profile.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class BookingForm(forms.ModelForm):
    seat_category = forms.ChoiceField(choices=Train.SEAT_CATEGORY_CHOICES, required=True,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    ticket_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.HiddenInput())

    class Meta:
        model = Booking
        fields = ['passenger_name', 'email', 'seat_category', 'ticket_price']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}))
