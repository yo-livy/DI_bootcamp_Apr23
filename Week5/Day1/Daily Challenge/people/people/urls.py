from django.contrib import admin
from django.urls import path
from people_app.views import people, people_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', people),
    path('people/<int:id>', people_id)
]
