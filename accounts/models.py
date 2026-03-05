from django.db import models

# Create your models here.

class Student(models.Model):
    # ab likhlo properties

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    ph_no = models.CharField(max_length = 15)
    address = models.TextField(max_length=150) 

class Volunteer(models.Model):
    # ab likhlo properties

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    ph_no = models.CharField(max_length = 15)
    address = models.TextField(max_length=150) 
    

class Administrator(models.Model):
    # ab likhlo properties

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    ph_no = models.CharField(max_length = 15)
    address = models.TextField(max_length=150) 
    

