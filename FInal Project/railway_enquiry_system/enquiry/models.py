from django.contrib.auth.models import User
from django.db import models

class Train(models.Model):
    SEAT_CATEGORY_CHOICES = [
        ('SL', 'Sleeper'),
        ('FC', 'First Class'),
        ('SC', 'Second Class'),
        ('1T', '1st Tier'),
    ]
    STATUS_CHOICES = [
        ('On Time', 'On Time'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
    ]

    train_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=50)
    available_seats = models.PositiveIntegerField(default=50)
    is_cancelled = models.BooleanField(default=False)
    sleeper_price = models.DecimalField(max_digits=8, decimal_places=2, default=100)
    first_class_price = models.DecimalField(max_digits=8, decimal_places=2, default=200)
    second_class_price = models.DecimalField(max_digits=8, decimal_places=2, default=150)
    first_tier_price = models.DecimalField(max_digits=8, decimal_places=2, default=300)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Time')

    def __str__(self):
        return f"{self.name} ({self.train_number})"

class Booking(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.passenger_name} on {self.train.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'