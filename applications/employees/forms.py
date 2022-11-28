from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model  = Employee
        # fields = ('__all__')
        fields = ["first_name","last_name","job","department","skills",]

        # I can access and modify the html attributes from the 'widgets' context variable
        widgets = {
            # Example: 'first_name' is how I declared the field in the model
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder': "Primer nombre ... ",
                    
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'placeholder': "Apellido ... "
                }
            )
        }

    # One of the ways to perform form validations
    def clean_department(self):
        department = self.cleaned_data['department']
        if department.name == 'Analisis en Servicios TI':
            raise forms.ValidationError('No hay vacantes disponibles en "Analisis en Servicios TI"')

        return department