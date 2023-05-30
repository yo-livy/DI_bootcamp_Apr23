from django.shortcuts import render
from info.models import Animal, Family

# Create your views here.

def family(request, id:int):
    
    data = Family.objects.all()
    context = {}
    context['data'] = []
    for element in data:
        if element['id'] == id:
            context['data'].append(element)
    return render(request, 'family.html', context)

def animal(request, id:int):
    data = Animal.objects.all()
    context = {}
    context['data'] = data
    for element in data:
        if element['id'] == id:
            context['data'] = element
    return render(request, 'animal.html', context)

def animals(request):
    data = Animal.objects.all()
    context = {
        'data': data
    }
    return render(request,'animals.html', context)
