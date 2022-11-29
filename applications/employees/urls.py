"""applications.employees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "employee_app"

urlpatterns = [
    path('todos/', views.ListAllEmployees.as_view(), name = 'employees_all'),
    path('por-departamento/<department_short_name>/', views.ListByDepartment.as_view(), name = 'employees_by_department'),
    # path('buscar-empleado/', views.ListByKeyword.as_view(), name = "employees_by_keyword"),
    path('habilidades-empleado/', views.ListSkillsOfEmployee.as_view(), name = 'employee_skills'),
    path('detalle-empleado/<pk>/', views.EmployeeDetail.as_view(), name = 'employee_detail'),
    path('registrar-empleado/', views.EmployeeCreate.as_view()),
    path('success/', views.CreateSuccess.as_view(), name = 'employee_success'),
    path('actualizar-empleado/<pk>/', views.EmployeeUpdate.as_view(), name = 'employee_update'),
    path('eliminar-empleado/<pk>/', views.EmployeeDelete.as_view(), name = 'employee_delete')
]

