from django import forms
from .models import EmployeeList


class EmployeeListForm(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = ['employee_id', 'name', 'description', 'image']

class EmployeeListFormEdit(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = ['name', 'description', 'image'] 
