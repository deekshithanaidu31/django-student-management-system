from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    course = models.CharField(max_length=40)
    age = models.IntegerField()
    batch = models.IntegerField()

    def __str__(self):
        return self.name
