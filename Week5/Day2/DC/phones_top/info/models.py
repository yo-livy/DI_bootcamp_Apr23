from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
