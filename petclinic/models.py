from django.db import models
from django.urls import reverse
from enum import Enum

# Create your models here.

class Sex(Enum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Owner(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('petclinic:owner', kwargs={'pk': self.pk})

class Animal(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sex = models.IntegerField(choices=Sex.choices(), default=Sex.UNKNOWN)

    def __str__(self):
        return self.name
