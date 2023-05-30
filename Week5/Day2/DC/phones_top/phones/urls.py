
from django.contrib import admin
from django.urls import path
from info.views import phonenumber, name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/phonenumber/<str:number>/', phonenumber, name="phone"),
    path('persons/name/<str:input_name>/', name, name='name'),
]
