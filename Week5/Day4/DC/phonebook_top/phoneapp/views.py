from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def person_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        persons = Person.objects.filter(
            models.Q(phone_number__contains=search_query) |
            models.Q(name__icontains=search_query)
        )
    else:
        persons = None

    context = {
        'persons': persons
    }
    return render(request, 'person_search.html', context)