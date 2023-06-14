#urls.py
from django.contrib import admin
from django.urls import path, include
from manage_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/department/', DepartmentListView.as_view(), name='department'),
    path('api/department/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('api/employee/', EmployeeListView.as_view(), name='employee'),
    path('api/employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('api/task/', TaskListView.as_view(), name='task'),
    path('api/task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('api/project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')
]


