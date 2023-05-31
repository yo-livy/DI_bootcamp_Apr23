from django.contrib import admin
from django.urls import path
from gifs.views import add_category_view, add_gif_view, homepage, category, categories, gif

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-category/', add_category_view),
    path('add-gif/', add_gif_view),
    path('homepage/', homepage),
    path('category/<int:cat_id>', category),
    path('categories', categories),
    path('gif/<int:gif_id>', gif)
]
