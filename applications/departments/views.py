from django.shortcuts import render
from django.views.generic.edit import FormView
from applications.employees.models import Employee
from .forms import CreateDepartmentForm
from .models import Department


class DepartmentCreate(FormView):
    template_name = 'departments/create.html'
    form_class    =  CreateDepartmentForm
    success_url   = '/'

    def form_valid(self, form):
        # Create the department
        department = Department(
            name = form.cleaned_data["name"],
            short_name = form.cleaned_data["short_name"]
        )
        department.save()

        # Create the employee
        # By using create d this way, you don't need to do 'save()' afterwards to save to the DB
        Employee.objects.create( 
            first_name = form.cleaned_data["first_name"],
            last_name = form.cleaned_data["last_name"],
            job = '1',
            department = department,
            full_name  = form.cleaned_data["first_name"] + " " + form.cleaned_data["last_name"]
        )
        
        
        
        return super(DepartmentCreate, self).form_valid(form)