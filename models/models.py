from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name