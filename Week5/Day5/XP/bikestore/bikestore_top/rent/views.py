from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def list_of_rentals(request):

    list_of_rentals = Rental.objects.all()

    context = {
        'list_of_rentals' : list_of_rentals
    }

    return render(request, 'list_of_rentals.html', context)

def list_of_rentals_id(request, rental_id:int):

    list_of_rentals_id = Rental.objects.get(id = rental_id)

    context = {
        'element_from_rentals_id' : list_of_rentals_id,
        'rental_id' : rental_id
    }

    return render(request, 'list_of_rentals_id.html', context)

def all_customers(request):
    all_customers = Customer.objects.order_by('last_name')
    # all_customers_sorted = sorted(all_customers, key=lambda x: x.last_name)
    context = {
        'all_customers' : all_customers
    }
    return render(request, 'all_customers.html', context)

def customer(request, customer_id):
    customer = Customer.objects.get(id = customer_id)
    rentals = Rental.objects.filter(customer_id = customer)
    context = {
        'customer' : customer,
        'customer_id' : customer_id,
        'rentals' : rentals
    }
    return render(request, 'customer.html', context)

def vehicle_id(request, vehicle_id):
    vehicle = Vehicle.objects.get(id = vehicle_id)
    available = check_availability(vehicle)


    context = {
        'vehicle' : vehicle,
        'vehicle_id' : vehicle_id,
        'available' : available
    }

    return render(request, 'vehicle_id.html', context)

def all_vehicles_grouped(request):

    vehicles = Vehicle.objects.order_by('vehicle_type')
    available = {}
    for i in vehicles:
        available[i.id] = check_availability(i)

    context = {
        'vehicles' : vehicles,
        'available' : available
    }

    return render(request, 'all_vehicles_grouped.html', context)

def add_rental(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = RentalForm(data)
        filled_form.save()

    form = RentalForm()
    context = {'form': form}
    return render(request, 'add_rental.html', context)


def add_customer(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = CustomerForm(data)
        if filled_form.is_Valid():
            filled_form.save()

    form = CustomerForm()
    context = {'form': form}
    return render(request, 'add_customer.html', context)

def add_vehicle(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = VehicleForm(data)
        filled_form.save()

    form = VehicleForm()
    context = {'form': form}
    return render(request, 'add_vehicle.html', context)
