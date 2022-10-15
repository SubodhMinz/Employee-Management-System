from django.shortcuts import render
from .models import Employee
from .forms import EmployeeAddForm, EmployeeFilterForm1, EmployeeFilterForm2


def home(request):
    return render(request, 'app/base.html')


def all_emp(request):
    employees = Employee.objects.all()
    return render(request, 'app/all_emp.html', {'employees':employees})


def add_emp(request):
    if request.method == "POST":
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
    form = EmployeeAddForm()
    return render(request, 'app/add_emp.html', {'form':form})


def remove_emp(request, id=None):
    if request.method == "POST":
        obj = Employee.objects.get(pk=id)
        obj.delete()
    employees = Employee.objects.all()
    return render(request, 'app/remove_emp.html', {'employees':employees})


def filter_emp(request):

    employees = Employee.objects.all()
    form1 = EmployeeFilterForm1()
    form2 = EmployeeFilterForm2()
    employees2 = None
    employees1 = None

    if request.method == "POST":
        dept = request.POST['dept']
        role = request.POST['role']
        print(dept)
        try:
            employees2 = employees.filter(role=role)
        except Exception as e:
            pass
        try:
            employees1 = employees.filter(dept=dept)
        except Exception as e:
            pass
        finally:
            context = {
                'employees2':employees2,
                'employees1':employees1,
                'form1':form1,
                'form2':form2
            }
            return render(request, 'app/filter_emp.html', context)
       
    context = {
        'employees':employees,
        'form1':form1,
        'form2':form2
    }
    return render(request, 'app/filter_emp.html', context)
