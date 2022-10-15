from django.contrib import admin
from .models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Employee)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'first_name', 
        'last_name', 
        'dept', 
        'salary', 
        'bonus', 
        'role', 
        'phone', 
        'hire_date'
        ]
