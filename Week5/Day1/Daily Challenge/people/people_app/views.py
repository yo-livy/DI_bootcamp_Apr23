from django.shortcuts import render
import requests

# Create your views here.

people_lst = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people(request):
    sorted_people = sorted(people_lst, key = lambda x: x['age'])
    context = {
        'sorted_people' : sorted_people
    }
    return render(request,'people.html', context)
