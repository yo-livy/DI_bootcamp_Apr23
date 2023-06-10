from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, GifForm
from .models import Gif, Category

# Create your views here.
def add_category_view(request):
    if request.method == 'POST':
                data = request.POST
                filled_form = CategoryForm(data)
                filled_form.save()

    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)


def add_gif_view(request):
    if request.method == 'POST':
                data = request.POST
                filled_form = GifForm(data)
                filled_form.save()

    category_form = GifForm()
    context = {'form': category_form}
    return render(request, 'add_gif.html', context)

def homepage(request): 
    gif_img = Gif.objects.values_list('url', flat=True)
    context = {
           'gif_img': gif_img
           }
    return render(request, 'homepage.html', context)


def category(request, cat_id):
    context = {
        'category' : Category.objects.get(id = cat_id)
    }
    return render(request, 'category.html', context)

def categories(request):
    context = {
        'category' : Category.objects.all()
    }
    return render(request, 'categories.html', context)


def gif(request, gif_id):
      
      
      context = {     
            'gif' : Gif.objects.get(id = gif_id)
      }
      
      return render(request, 'gif.html', context)

def increment_likes(request, gif_id):
    gif = get_object_or_404(Gif, id=gif_id)
    gif.likes += 1
    gif.save()
    return redirect('gif', gif_id=gif_id)

def decrement_likes(request, gif_id):
    gif = get_object_or_404(Gif, id=gif_id)
    if gif.likes > 0:
        gif.likes -= 1
        gif.save()
    return redirect('gif', gif_id=gif_id)

def popular_gifs(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    context = {
        'gifs': gifs
    }
    return render(request, 'popular_gifs.html', context)