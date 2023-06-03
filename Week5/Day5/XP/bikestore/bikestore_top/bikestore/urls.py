

from django.contrib import admin
from django.urls import path
from rent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/', list_of_rentals, name='list_of_rentals'),
    path('rent/rental/<int:rental_id>/', list_of_rentals_id, name='list_of_rentals_id'),
    path('rent/customer/', all_customers, name='all_customers'),
    path('rent/customer/<int:customer_id>/', customer, name='customer'),
    path('rent/vehicle_id/<int:vehicle_id>/', vehicle_id, name='vehicle_id'),
    path('rent/rental/add/', add_rental, name='add_rental'),
    path('rent/customer/add/', add_customer, name='add_customer'),
    path('rent/vehicle/add/', add_vehicle, name='add_vehicle'),
    path('rent/vehicle/', all_vehicles_grouped, name='add_vehicles_grouped')

]

