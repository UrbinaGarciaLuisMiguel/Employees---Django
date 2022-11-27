from django.contrib import admin
from .models import Employee, Skills

# 'Employee' model registration in django admin panel

admin.site.register(Skills)


class EmployeAdmin(admin.ModelAdmin):
    # Customize field to display in admin panel
    list_display  = ('id','first_name','last_name','department','job','full_name',)
    # A browser for the model
    search_fields = ('first_name',)
    # Filter parameters
    list_filter   = ('job', 'skills',) 
    # Filter for 'skills' (works on many-to-many relationships)
    filter_horizontal = ('skills',)

    # Extra column in administrator panel that is not in the 'Employees' model defined
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

admin.site.register(Employee, EmployeAdmin)