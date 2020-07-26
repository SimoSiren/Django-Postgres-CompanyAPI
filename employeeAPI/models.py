from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_code = models.CharField(max_length=3)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=20)