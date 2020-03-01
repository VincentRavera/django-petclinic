#!/usr/bin/env python3
from django.urls import path

from . import views

app_name="petshop"
urlpatterns = [
    # /petshop/owner
    # List owners
    path('owner', views.IndexView.as_view(), name='index'),

    # /petshop/owner/5
    path('owner/<int:pk>', views.owner_view, name='owner'),

    # /petshop/owner/5/pet/1
    #path('/owner/<int:pk>/pet/<int:pk>', views.AnimalView.as_view(), name='animal'),

]
