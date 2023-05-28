from django.contrib import admin
from django.urls import path
from info.views import family, animal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/', family),
    path('animal/', animal)
]
