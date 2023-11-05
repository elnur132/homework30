from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True 
    
class Programmer(Human):
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    
class JuniorProgrammer(Programmer):
    experience = models.IntegerField()