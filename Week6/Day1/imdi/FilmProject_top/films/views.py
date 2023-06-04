from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
# Create a class-based view, HomePageView, which inherits from generic.ListView. This view should be used for the URL route: /homepage, and render a template called homepage.html.

class HomePageView(ListView):
    template_name = 'homepage.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.all()


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('homepage')

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('homepage')



