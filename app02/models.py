from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    class_name = models.ForeignKey(to='Class', to_field='id', on_delete=True)
    teacher = models.ManyToManyField(to='Teacher')

class Class(models.Model):
    title = models.CharField(max_length=32)

class Teacher(models.Model):
    name = models.CharField(max_length=32)