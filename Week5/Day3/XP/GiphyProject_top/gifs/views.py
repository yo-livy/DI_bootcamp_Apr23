from django.shortcuts import render
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