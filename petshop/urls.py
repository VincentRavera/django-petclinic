#!/usr/bin/env python3
from django.urls import path

from . import views

app_name="petshop"
urlpatterns = [
    # /petshop/owner
    path('', views.IndexView.as_view(), name='index'),
    # List owners
    path('owner', views.owner_list, name='owners'),

    # /petshop/owner/5
    path('owner/<int:pk>', views.owner_view, name='owner'),

    # /petshop/animal
    path('animal', views.animal_list, name='animals'),

    # /petshop/animal/7
    path('animal/<int:pk>', views.animal_view, name='animal'),

]
