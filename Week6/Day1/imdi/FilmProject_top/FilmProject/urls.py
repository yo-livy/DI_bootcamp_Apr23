from django.contrib import admin
from django.urls import path
from films.views import HomePageView, FilmCreateView, DirectorCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('add-film/', FilmCreateView.as_view(), name='add-film'),
    path('add-director/', DirectorCreateView.as_view(), name='add-director')
]
