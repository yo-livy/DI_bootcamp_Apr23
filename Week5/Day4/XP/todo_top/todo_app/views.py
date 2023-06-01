from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo, Category
import datetime

# Create your views here.

def todo(request):
    if request.method == 'POST':
        data = request.POST
        filled_form = TodoForm(data)
        filled_form.save()

    post_form = TodoForm()
    context = {'form': post_form}
    return render(request, 'todos.html', context)


def display_todos(request):
    todo_list = Todo.objects.all()

    context = {'todo_list':todo_list}

    return render(request, 'display_todos.html', context)

def todo_done(request, todo_id):

    todo = Todo.objects.get(id=todo_id)

    if request.method == "POST":
    
        if 'done' in request.POST:
            todo.has_been_done = True
            todo.date_completion = datetime.datetime.now()
            todo.save()

    return redirect('display_todos')
