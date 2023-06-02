from django.contrib import admin
from django.urls import path
from todo_app.views import todo, display_todos, todo_done

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('display-todos/', display_todos, name='display_todos'),
    path('todo-done/<int:todo_id>/', todo_done, name='todo_done')
]
