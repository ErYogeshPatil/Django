from django.db import models

# Create your models here.

# Table in database for product display
class Product(models.Model):
    Name=models.CharField(max_length=50)
    P_desc=models.CharField(max_length=100)
    Discount_Price=models.IntegerField()
    Actual_Price=models.CharField(max_length=50)
    Type=models.CharField(max_length=20)
    Offer=models.CharField(max_length=20)
    is_deleted=models.CharField(max_length=5)
    is_Cart=models.CharField(max_length=5)
    Image=models.CharField(max_length=40)


# --------------------------------------------------------------
# Table in database for User login
class User_Details(models.Model):
    User_Name=models.CharField(max_length=50)
    U_Email=models.CharField(max_length=50)
    U_Password=models.CharField(max_length=50)


# Table in database for Employee login
class Emp_Details(models.Model):
    E_Name=models.CharField(max_length=50)
    E_Role=models.CharField(max_length=50)
    E_Password=models.CharField(max_length=50)

