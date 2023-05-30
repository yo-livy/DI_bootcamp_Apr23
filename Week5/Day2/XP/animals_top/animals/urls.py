from django.contrib import admin
from django.urls import path
from info.views import family, animal, animals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<int:id>', family, name='family'),
    path('animals', animals, name='animals'),
    path('animal/<int:id>', animal, name='animal'),
]
