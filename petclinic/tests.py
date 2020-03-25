from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Owner, Animal

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
def clean_owners():
    for owner in owners_created:
        owner.delete()

def clean_animals():
    for animal in animals_created:
        animal.delete()

def clean_data():
    clean_owners()
    clean_animals()
# Views Tests
class OwnerViewTests(TestCase):

    def test_create(self):
        create_url = reverse('petclinic:ownercreate')
        post_data = {
            'name': 'foo',
            'number': '0',
        }
        response = self.client.post(create_url, data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Owner.objects.filter(name=post_data['name']).count(), 1)
        owner = Owner.objects.filter(name=post_data['name'])[0]
        self.assertEqual(owner.number, post_data['number'])

    def test_delete(self):
        name = 'foo'
        number = "0"
        owner = Owner(name=name, number=number)
        owner.save()
        delete_url = reverse('petclinic:ownerdelete', args=(owner.id,))
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        is_deleted = False
        try:
            Owner.objects.get(id=owner.id)
        except ObjectDoesNotExist:
            is_deleted = True
        self.assertTrue(is_deleted, "Was not deleted")
