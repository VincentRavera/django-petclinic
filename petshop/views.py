from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Owner

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'petshop/index.html.j2'
    context_object_name = 'owner_list'

    def get_queryset(self):
        return Owner.objects.all()

def owner_view(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    animals = owner.animal_set.all()
    return render(request, 'petshop/owner_view.html.j2', {'owner': owner, 'animals_list': animals})
