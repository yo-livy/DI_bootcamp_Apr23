from django.contrib import admin
from django.urls import path, include
from studentapp.views import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/students/', StudentView.as_view(), name='posts'),
    path('api/students/<int:pk>/', StudentView.as_view(), name='post-detail')
]
