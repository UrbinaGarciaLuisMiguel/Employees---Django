from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from applications.employees.models import Employee
from .forms import CreateDepartmentForm
from .models import Department

class ListAllDepartment(ListView ):
    template_name = 'departments/list_all.html'
    model         = Department
    paginate_by   = 3 # genera objeto (page_obj) para manejar la paginación en el template
    
    # This type of view (ListView) manages the entire list of records in the model, 
    # so I access it through the variable that I define in this field.
    context_object_name = 'list_departments'

    def get_queryset(self):
        # Receives the 'keyword' from the URL
        keyword = self.request.GET.get("keyword", "") # Keyword is the value 'name' of the html element containing the 'keyword'
        
        # <attribute_name>__icontains, filter the search with minimal matches
        # Ex: In an array "Paralelepipedo, Paral", where keyword = 'Paral'
        # would return the two words; but if the filtering were only "full_name" (Not full_name__icontains)
        # would only return word 2 ('Paral')
        list = Department.objects.filter( name__icontains = keyword ) 
        return list


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