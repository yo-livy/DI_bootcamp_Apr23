
from django.contrib import admin
from django.urls import path
from info.views import family, animal, animals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<int:id>', family),
    path('animal/<int:id>', animal),
    path('animals/', animals)
]
