import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore.settings')
import django
django.setup()

from rent.models import Rental, Vehicle, Customer
from faker import Faker
import random
import datetime

fake = Faker()

while len(Rental.objects.all()) < 100:

    vehicle = random.choice(Vehicle.objects.all())

    rental_date = fake.past_date()
    return_date = fake.past_date(start_date=rental_date)

    if random.randint(0, 1) == 1:
        return_date = None


    rental_list = Rental.objects.filter(vehicle=vehicle.id)

    if len(rental_list) > 0:
        if rental_list.filter(return_date__isnull=True).count() > 0:
            continue

        latest_rental = Rental.objects.select_related('vehicle').filter(vehicle=vehicle.id).latest('return_date')

        if latest_rental.return_date >= rental_date:
            continue

    rental = Rental(
        rental_date=rental_date,
        return_date=return_date,
        customer=random.choice(Customer.objects.all()),
        vehicle=vehicle
    )
    rental.save()