from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin





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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ProducerFormSet()
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        formset = ProducerFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)
        
    
        





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



class FilmDetailView(DetailView):
    model = Film
    template_name = 'film/film_detail.html'  # Specify the template for rendering film details
    context_object_name = 'film'  # Set the variable name to use in the template for the film object

# def producers(request):
#     #POST
#     if request.method == 'POST':
#         formset = ProducerFormSet(request.POST, queryset=Producer.objects.all())
#         if formset.is_valid():
#             instances = formset.save(commit=False)
#             for instance in instances:
#                 instance.save()
#             context = {'formset': formset}
#             return render(request, 'film/producers.html', context)
#         else:
#             print(formset.errors)
#     #GET
#     formset = ProducerFormSet(queryset=Producer.objects.all())
#     context = {'formset': formset}
#     return render(request, 'film/producers.html', context)
