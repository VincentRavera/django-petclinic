from django.urls import reverse_lazy
from django.views import generic

from .models import Owner, Animal

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'petshop/index.html'
    context_object_name = 'owner_list'

    def get_queryset(self):
        """Returns all Owner"""
        return Owner.objects.all()

class OwnerView(generic.ListView):
    template_name = 'petshop/owner_list.html'
    context_object_name = 'owner_list'

    def get_queryset(self):
        "Returns all Owner"
        return Owner.objects.all()


class OwnerDetail(generic.DetailView):
    template_name = 'petshop/owner_view.html'
    model = Owner


class OwnerCreate(generic.CreateView):
    model = Owner
    fields = ['name', 'number']


class OwnerDelete(generic.DeleteView):
    model = Owner
    success_url = reverse_lazy('petshop:owners')


class AnimalView(generic.ListView):
    template_name = 'petshop/animal_list.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        return Animal.objects.all()


class AnimalDetail(generic.DetailView):
    template_name = 'petshop/animal_view.html'
    model = Animal
