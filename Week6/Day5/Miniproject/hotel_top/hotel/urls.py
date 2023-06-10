
from django.contrib import admin
from django.urls import path
from visitors.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info, name='info'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('book-stay/', login_required(booking), name='book-stay'),
    path('rooms/<int:id>/', rooms, name='rooms'),
    path('rooms-all/', rooms_all, name='rooms-all'),
    path('contact/', contact_view, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)