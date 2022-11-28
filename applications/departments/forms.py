from django import forms

class CreateDepartmentForm(forms.Form):

    name       = forms.CharField(max_length = 50)
    short_name = forms.CharField(max_length = 20)
    
    # Under the statement that a department is created when there is at least 
    # one employee in it, fields are added to request data from the 'employee'
    first_name = forms.CharField(max_length = 50)
    last_name  = forms.CharField(max_length = 50)