
from django.contrib import admin
from django.urls import path, include
from book_review_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('info/', info, name='info'),
    path('info/<int:pk>/', info_detail, name='info-detail'),
    path('add-review/', add_review, name='add-review'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]
