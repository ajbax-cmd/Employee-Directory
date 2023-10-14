from django.db import models
import random

# Create your models here.
def generate_employee_id():
    # Define a suitable range for the random numbers. Adjust as necessary.
    min_id = 152964
    max_id = 999999
    # Generate a random employee ID.
    employee_id = random.randint(min_id, max_id)
    # Keep generating new numbers while the employee_id already exists.
    while EmployeeList.objects.filter(employee_id=employee_id).exists():
        employee_id = random.randint(min_id, max_id)

    return employee_id


class EmployeeList(models.Model):
    employee_id = models.PositiveIntegerField(unique=True, default=generate_employee_id)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='employee_pictures/')