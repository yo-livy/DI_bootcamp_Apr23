from django.contrib import admin
from django.urls import path
from gifs.views import add_category_view, add_gif_view, homepage, category, categories, gif, increment_likes, decrement_likes, popular_gifs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-category/', add_category_view),
    path('add-gif/', add_gif_view),
    path('homepage/', homepage),
    path('category/<int:cat_id>', category),
    path('categories', categories),
    path('gif/<int:gif_id>', gif, name='gif'),
    path('gif/increment_likes/<int:gif_id>/', increment_likes, name='increment_likes'),
    path('gif/decrement_likes/<int:gif_id>/', decrement_likes, name='decrement_likes'),
    path('popular-gifs/', popular_gifs, name='popular-gifs')
]
