from .models import Employee
from django import forms

class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeFilterForm1(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['dept']

class EmployeeFilterForm2(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['role']