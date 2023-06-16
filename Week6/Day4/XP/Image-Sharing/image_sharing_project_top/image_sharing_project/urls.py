from django.contrib import admin
from django.urls import path, include
from image_share.views import *
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('upload/', upload_image, name='upload_image'),
    path('images/', view_images, name='view_images'),
    path('myimages/', my_images, name='my_images'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
