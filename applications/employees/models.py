from django.db import models
# Related model import
from applications.departments.models import Department



# Model for table 'Skills'
class Skills(models.Model):
    skill =  models.CharField("Habilidad", max_length = 50)

    # Adaptation to show in the administrator panel
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = "Skills"

    def __str__(self):
         return self.skill


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
    full_name  = models.CharField("Nombre Completo", max_length = 100)
    avatar     = models.ImageField(upload_to = 'employees', blank = True, null = True) 
    job        = models.CharField("Cargo", max_length  = 1, choices = JOB_CHOICES)
    
    # Foreign keys
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    skills     =  models.ManyToManyField(Skills)
    
    # Adaptation to show in the administrator panel
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = "Empleados"

    def __str__(self):
         return '(' + str(self.id) + ') ' + self.first_name + " " +self.last_name
