
from django.contrib import admin
from django.urls import path
from manage_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/department/', DepartmentListView.as_view(), name='department'),
    path('api/employee/', EmployeeListView.as_view(), name='employee'),
    path('api/task/<int:pk>/', TaskListView.as_view(), name='task'),
    path('api/project/<int:pk>/', ProjectListView.as_view(), name='project')
]
