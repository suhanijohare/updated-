from django.db import models
import datetime 

# Create your models here.
from django.db import models

class Patient(models.Model):
    # model fields here
    pass

class Driver(models.Model):
    # model fields here
    pass

class Paramedic(models.Model):
    # model fields here
    pass

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hospital = models.CharField(max_length=100)
    hospital_id = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Use a hashed password in a real app

    def __str__(self):
        return self.username

  