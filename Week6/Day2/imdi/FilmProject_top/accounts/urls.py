from django.urls import path
from django.contrib.auth import views
from .views import SignupView

urlpatterns = [
   path('signup/', SignupView.as_view(), name='signup'),
   path('login/', views.LoginView.as_view(template_name='login.html') , name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout')
#    path('profile/<int:id>', , name='profile')
]
