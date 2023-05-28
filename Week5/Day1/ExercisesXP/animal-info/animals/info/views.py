from django.shortcuts import render
import requests
import json
# Create your views here.

def family(request):
    file_path = '/Users/yo.livy/Desktop/Week5/Day1/ExercisesXP/animal-info/animals/info/animals.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    context = {}
    return render(request, 'family.html', context)

def animal(request):
    file_path = '/Users/yo.livy/Desktop/Week5/Day1/ExercisesXP/animal-info/animals/info/animals.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    context = {
        'animals': data['animals']
    }
    return render(request, 'animal.html', context)
