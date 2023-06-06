from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



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



class FilmDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
   
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False
    
    model = Film
    template_name = 'film/film_confirm_delete.html'
    success_url = reverse_lazy('homepage')
    success_message = "Film deleted successfully."


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('homepage')


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    success_url = reverse_lazy('homepage')


