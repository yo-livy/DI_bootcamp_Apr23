from django.shortcuts import render
from .models import Person

# Create your views here.

def by_name(request, name:str):
    person = None
    try:
        person = Person.objects.get(name=name_search)
    except Person.DoesNotExist:
        pass
    return render(request, 'name.html', context)

def by_number(request, phonenumber:str):
    pass

