from django.db import models
import psycopg2

# Create your models here.

class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)

class Family(models.Model):
    name = models.CharField(20)