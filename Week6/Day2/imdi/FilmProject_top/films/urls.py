from django.urls import path
from films.views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('add-film/', FilmCreateView.as_view(), name='add-film'),
    path('add-director/', DirectorCreateView.as_view(), name='add-director'),
    path('add-review/', ReviewCreateView.as_view(), name='add-review')
]
