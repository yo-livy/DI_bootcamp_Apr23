from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def info(request):
    
    hotels = Hotel.objects.all()
    context = {
        'hotels' : hotels
    }

    return render(request, 'info.html', context)


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)

            # Check room availability
            room = booking.room
            check_in_date = booking.check_in_date
            check_out_date = booking.check_out_date

            # Check if the room is available for the specified date range
            if is_room_available(room, check_in_date, check_out_date):
                booking.user = request.user
                booking.save()
                return render(request, 'booking/success.html')
            else:
                return render(request, 'booking/availability_error.html')
    else:
        form = BookingForm(user=request.user)
    
    
    context = {
        'form': form
        }

    return render(request, 'booking/book_stay.html', context)


def is_room_available(room, check_in_date, check_out_date):
    # Check if any overlapping bookings exist for the specified room and date range
    overlapping_bookings = Booking.objects.filter(
        room=room,
        check_in_date__lt=check_out_date,
        check_out_date__gt=check_in_date
    )
    
    return not overlapping_bookings.exists()


def rooms(request, id:int):
    
    room = Room.objects.get(id=id)
    available = Availability.objects.filter(room_id=room.id).order_by('date')
    
    context = {
        'room' : room,
        'available' : available
    }

    return render(request, 'rooms.html', context)

def rooms_all(request):
    rooms_all = Room.objects.all()

    context = {
        'rooms_all' : rooms_all
    }

    return render(request, 'rooms_all.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html') # Redirect to a success page or display a success message
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact_form.html', context)
