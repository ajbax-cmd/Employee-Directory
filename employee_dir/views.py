from django.shortcuts import render, redirect, HttpResponse
from django import forms
from .forms import EmployeeListForm
from .forms import EmployeeListFormEdit
from .models import EmployeeList
from django.shortcuts import get_object_or_404
from django.db.models import Q







# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def delete_employee(request, employee_id):
    employee = get_object_or_404(EmployeeList, id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_directory')  # assuming 'employee_directory' is the name of the view where all employees are listed

    context = {'employee': employee}
    return render(request, 'delete_employee.html', context)

def edit_employee(request, employee_id):
    employee = get_object_or_404(EmployeeList, id=employee_id)
    if request.method == 'POST':
        form = EmployeeListFormEdit(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_directory')
    else:
        form = EmployeeListFormEdit(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})


def employee_directory(request):
    employees = EmployeeList.objects.all()

    # Sorting
    sort_by = request.GET.get('sort_by', 'employee_id')
    if sort_by == 'employee_id':
        employees = employees.order_by(sort_by)
    elif sort_by == 'name':
        employees = sorted(employees, key=lambda e: e.name.split()[-1])

    # Searching
    search_term = request.GET.get('search')
    if search_term:
        try:
            search_id = int(search_term)
            employees = employees.filter(Q(name__icontains=search_term) | Q(employee_id=search_id))
        except ValueError:
            employees = employees.filter(name__icontains=search_term)

    return render(request, "employee_directory.html", {"employees": employees})




def contact_view(request):
    if request.method == "POST":
        form = EmployeeListForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_directory')
    else:
        form = EmployeeListForm()

    return render(request, 'contact_template.html', {'form': form})


def add_employee(request):
    if request.method == "POST":
        form = EmployeeListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_directory')  # Redirect to employee list after adding

    else:
        form = EmployeeListForm()

    return render(request, 'add_employee.html', {'form': form})
