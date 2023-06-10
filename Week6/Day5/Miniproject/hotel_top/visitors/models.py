from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Hotel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='hotel_photos')

    def __str__(self):
        return self.title
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.hotel.title}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.room} ({self.check_in_date} to {self.check_out_date})"


class Availability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='availability')
    date = models.DateField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.room} - {self.date} ({'Available' if self.available else 'Not Available'})"


@receiver(post_save, sender=Booking)
def update_availability_on_booking_create(sender, instance, created, **kwargs):
    if created:
        # Get all the overlapping availability instances
        overlapping_availabilities = Availability.objects.filter(
            room=instance.room,
            date__range=[instance.check_in_date, instance.check_out_date]
        )
        
        # Iterate through the overlapping availabilities and update their availability
        for availability in overlapping_availabilities:
            availability.available = False
            availability.save()


@receiver(post_delete, sender=Booking)
def update_availability_on_booking_delete(sender, instance, **kwargs):
    # Get all the overlapping availability instances
    overlapping_availabilities = Availability.objects.filter(
        room=instance.room,
        date__range=[instance.check_in_date, instance.check_out_date]
    )
    
    # Iterate through the overlapping availabilities and update their availability
    for availability in overlapping_availabilities:
        availability.available = True
        availability.save()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


