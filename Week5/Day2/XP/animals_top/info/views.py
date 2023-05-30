from django.shortcuts import render
from .models import Animal, Family


def animals(request):
    context = {
        'animals_all' : Animal.objects.all()
    }
    return render(request, 'animals.html', context)


def animal(request, id):
    context = {
        'animal_one' : Animal.objects.get(id = id)
    }
    return render(request, 'animal.html', context)

def family(request, id):
    context = {
        'family' : Family.objects.get(id = id),
        'animals' : Animal.objects.filter(family = id)
    }
    return render(request, 'family.html', context)

