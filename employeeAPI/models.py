from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_code = models.CharField(max_length=3)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=20)

class Customer(models.Model):
    customer_code = models.CharField(max_length=3)
    companyname = models.CharField(max_length=50)
    contactname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Product(models.Model):
    product_code = models.CharField(max_length=3)
    productname = models.CharField(max_length=50)
    quantity_per_unit = models.CharField(max_length=50)
    units_in_stock = models.IntegerField()
    price = models.IntegerField()