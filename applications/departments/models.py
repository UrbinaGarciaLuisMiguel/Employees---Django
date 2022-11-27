from django.db import models

# Model for table 'departments'
class Department(models.Model):

    name = models.CharField("Nombre", max_length=50)
    # Single field, will not be repeated
    short_name  = models.CharField("Nombre Corto", max_length=20, unique=True)
    is_inactivo = models.BooleanField("Inactivo", default = False)

    # Adaptation to show in the administrator panel
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return '(' + str(self.id) + ')   ' + self.name
    