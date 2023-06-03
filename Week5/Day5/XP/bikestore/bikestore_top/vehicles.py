import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikestore.settings")
import django
django.setup()

from rent.models import Vehicle, VehicleType, VehicleSize
import random

def add_vehicles(number):
    for i in range(number):
        vehicle = Vehicle(
            vehicle_type=random.choice(VehicleType.objects.all()),
            size=random.choice(VehicleSize.objects.all()),
            real_cost=random.randint(300, 5000)
        )
        vehicle.save()
    print(f"{number} vehicles was created")

add_vehicles(220)