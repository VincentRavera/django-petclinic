#!/usr/bin/env python3
from django.urls import path

from . import views

app_name="petshop"
urlpatterns = [
    # /petshop/owner
    path('', views.IndexView.as_view(), name='index'),
    # List owners
    path('owner', views.OwnerView.as_view(), name='owners'),

    # /petshop/owner/5
    path('owner/<int:pk>', views.OwnerDetail.as_view(), name='owner'),

    # /petshop/animal
    path('animal', views.AnimalView.as_view(), name='animals'),

    # /petshop/animal/7
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name='animal'),

]
