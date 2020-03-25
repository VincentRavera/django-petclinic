from django.test import TestCase
from .models import Owner, Animal, RendezVous

# Create your tests here.

# Utils Functions

owners_created = []
def create_owner(name, number):
    """
    Create an Owner with the given `name` and his phone `number`.
    """
    owner = Owner.objects.create(name=name, number=number)
    owners_created.append(owner)
    return owner
animals_created = []
def create_animal(name, number):
    """
    Create an Animal with the given `name` and his phone `number`.
    """
    animal = Animal.objects.create(name=name, number=number)
    animals_created.append(animal)
    return animal
rendezVouss_created = []
def create_rendezVous(name, number):
    """
    Create an RendezVous with the given `name` and his phone `number`.
    """
    rendezVous = RendezVous.objects.create(name=name, number=number)
    rendezVouss_created.append(rendezVous)
    return rendezVous

def clean_owners():
    for owner in owners_created:
        owner.delete()

def clean_animals():
    for animal in animals_created:
        animal.delete()

def clean_rendezVouss():
    for rendezVous in rendezVouss_created:
        rendezVous.delete()

def clean_data():
    clean_owners()
    clean_animals()
    clean_rendezVouss()
# Views Tests

# Models test
class OwnerModelTests(TestCase):
    pass
class AnimalModelTests(TestCase):
    pass
class RendezVousModelTests(TestCase):
    pass
