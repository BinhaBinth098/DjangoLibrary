from django.db import models

# Create your models here.
class Employee(models.Model):
    emid=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="image")