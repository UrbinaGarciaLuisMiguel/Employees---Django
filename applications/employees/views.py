from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy


""" List all the employees of the company """
class ListAllEmployees(ListView):
    # Name of the template associated with this view
    template_name = 'employees/list_all.html'
    model         = Employee
    # This type of view (ListView) manages the entire list of records in the model, 
    # so I access it through the variable that I define in this field.
    context_object_name = 'list_employees'


""" List all employees belonging to a company department """
class ListByDepartment(ListView):
    # Name of the template associated with this view
    template_name = 'employees/list_by_department.html'
    
    # Filter list of employees, by 'department'
    # queryset      = Employee.objects.filter( department__name = 'Contabilidad y Finanzas interiores' ) # Two underscores (__) and then the model attribute (name)
    def get_queryset(self):
        # Receives the 'short_name' from the URL
        department = self.kwargs['department_short_name']
        list = Employee.objects.filter( department__short_name = department ) # Two underscores (__) and then the model raltionsship attribute (short_name)
        return list
    
    # This type of view (ListView) manages the entire list of records in the model, 
    # so I access it through the variable that I define in this field.
    context_object_name = 'list_employees_by_deparment'


""" List of employees by keyword """
class ListByKeyword(ListView):
    template_name       = 'employees/list_by_keyword.html'
    context_object_name = 'list_employees_by_keyword'

    def get_queryset(self):
        # Receives the 'keyword' from the URL
        keyword = self.request.GET.get("keyword", "") # Keyword is the value 'name' of the html element containing the 'keyword'
        list = Employee.objects.filter( first_name = keyword ) 
        return list

""" List skills of an employee """
class ListSkillsOfEmployee(ListView):
    template_name       = 'employees/list_skills.html'
    context_object_name = 'list_skills'

    def get_queryset(self):
        # Receives the 'keyword' from the URL
        employee_id = self.request.GET.get("employee", "") # employee_id is the value 'name' of the html element containing the employee id
        if employee_id != '':
            employee = Employee.objects.get(id = employee_id )
            return employee.skills.all()
        return []

class EmployeeDetail(DetailView):
    template_name       = 'employees/detail_employee.html'
    model               = Employee
    context_object_name = 'object_detail'


class CreateSuccess(TemplateView):
    template_name = 'employees/success.html'


class EmployeeCreate(CreateView):
    template_name = 'employees/create.html'
    model         = Employee
    # Extra field queredio in the 'CreateView', referred to the model attributes
    # fields        = ('__all__')
    fields = ["first_name","last_name","job","department","skills"] # The 'fields' decorator handles a default variable
                                                                    # called 'form' referring to the fields indicated in 
                                                                    # its declaration. it can be accessed in the .html 
                                                                    # template

    # I must indicate which URL to go to when the request is successfully completed
    # success_url = '/employees/success' # Redirect to the same page
    success_url   = reverse_lazy('employee_app:employee_success') 


    def form_valid(self, form):
        employee = form.save(commit = False) # Creates instance as it will go to database, but doesn't waste memory on save
        employee.full_name = employee.first_name + " " + employee.last_name
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeUpdate(UpdateView):
    template_name = 'employees/update.html'
    model         = Employee
    fields = ["first_name","last_name","job","department","skills"]
    success_url   = reverse_lazy('employee_app:employee_success')


    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     print(request.POST) # I can access the values ​​received by the 'request'
    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        employee = form.save(commit = False) # Creates instance as it will go to database, but doesn't waste memory on save
        employee.full_name = employee.first_name + " " + employee.last_name
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeDelete(DeleteView):
    model = Employee
    # When 'delete' it is sometimes necessary to confirm the deletion, for this reason a 'template_name' is silvered
    template_name = 'employees/delete.html'
    success_url = reverse_lazy('employee_app:employee_success')