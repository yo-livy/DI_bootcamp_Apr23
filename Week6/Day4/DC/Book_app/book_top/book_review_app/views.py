from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Avg, Count


# Create your views here.
def info(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'info.html', context)

def info_detail(request, pk:int):
    book = Book.objects.get(id=pk)
    average_rating = book.bookreview_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
    review_count = book.bookreview_set.aggregate(review_count=Count('id'))['review_count']
    
    context = {
        'book' : book,
        'average_rating': average_rating,
        'review_count': review_count
    }
    return render(request, 'info_detail.html', context)


def add_review(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = BookReviewForm(data)
        filled_form.save()

    form = BookReviewForm()
    context = {'form': form}
    return render(request, 'add_review.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
