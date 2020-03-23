from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Owner, Animal

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'petshop/index.html'
    context_object_name = 'owner_list'

    def get_queryset(self):
        """Returns all Owner"""
        return Owner.objects.all()


def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'petshop/owner_list.html', {'owner_list': owners})


def owner_view(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    animals = owner.animal_set.all()
    return render(request, 'petshop/owner_view.html', {'owner': owner, 'animals_list': animals})

def animal_view(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'petshop/animal_view.html', {'animal': animal})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'petshop/animal_list.html', {'animal_list': animals})
