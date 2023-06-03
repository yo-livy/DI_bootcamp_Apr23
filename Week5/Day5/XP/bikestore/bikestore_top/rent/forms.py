from django import forms
from .models import *

def check_availability(vehicle):

    rentals = Rental.objects.filter(vehicle=vehicle.id)

    if len(rentals) == 0:
        return True
    else:
        if not rentals.filter(return_date__isnull=True).count() > 0:
            return True
    return False


def get_available_vehicles():
    available_vehicles_ids = list()

    all_vehicles = Vehicle.objects.all()

    for vehicle in all_vehicles:
        if check_availability(vehicle):
            available_vehicles_ids.append(vehicle.id)

    return Vehicle.objects.filter(id__in=available_vehicles_ids)


class RentalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = get_available_vehicles()




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


