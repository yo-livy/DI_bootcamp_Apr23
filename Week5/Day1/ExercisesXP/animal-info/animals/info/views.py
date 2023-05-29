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

def animals(request, id):
    with open('/Users/yo.livy/Desktop/Week5/Day1/ExercisesXP/animal-info/animals/info/animals.json') as file:
        data = json.load(file)
    
    for animal in data['animals']:
        if animal['id'] == int(id):
            context = {"Name": animal['name'],
                           "Legs": animal['legs'],
                            "Weight": animal['weight'],
                            "Height": animal['height'],
                             "Speed": animal['speed']}
    return render(request, 'animal.html', context)
