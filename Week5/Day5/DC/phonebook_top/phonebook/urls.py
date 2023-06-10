
from django.contrib import admin
from django.urls import path
from phoneapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person-search', person_search, name='person-search')
]
