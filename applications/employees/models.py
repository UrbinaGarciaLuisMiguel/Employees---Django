from django.db import models
# Related model import
from applications.departments.models import Department

# Model for table 'Employees'
class Employee(models.Model):
    # Choice
    JOB_CHOICES = (
        ('O', 'Generente'),
        ('1', "Administrador"),
        ('2', "Analista"),
        ('3', "Obrero"),
        ('4', "Contador"),
    )

    first_name = models.CharField("Nombre", max_length = 50)
    last_name  = models.CharField("Apellido", max_length = 50)
    job        = models.CharField("Cargo", max_length  = 1, choices = JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    # image      = models.ImageField("Imagen", upload_to = None, height_field = None, width_field = None) 

    def __str__(self):
         return '(' + str(self.id) + ') ' + self.first_name + " " +self.last_name
