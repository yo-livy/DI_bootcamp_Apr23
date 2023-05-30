from django.shortcuts import render
from .models import Person

# Create your views here.
def phonenumber(request, number):

    try:
        person = Person.objects.get(phone_number = number)
    except Person.DoesNotExist:
        person = None

    context = {
        'person' : person
    }

    return render(request, 'number.html', context)

def name(request, input_name):
    try: 
        person = Person.objects.get(name = input_name)
    except Person.DoesNotExist:
        person = None

    context = {
        'person' : person
    }

    return render(request, 'name.html', context)

