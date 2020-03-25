#!/usr/bin/env python3
from django.urls import path

from . import views

app_name="petclinic"
urlpatterns = [
    # /petclinic/owner
    path('', views.IndexView.as_view(), name='index'),
    # List owners
    path('owner', views.OwnerView.as_view(), name='owners'),

    # /petclinic/owner/5
    path('owner/<int:pk>', views.OwnerDetail.as_view(), name='owner'),

    # /petclinic/owner/create
    path('owner/create', views.OwnerCreate.as_view(), name='ownercreate'),

    # /petclinic/owner/delete
    path('owner/<int:pk>/delete', views.OwnerDelete.as_view(), name='ownerdelete'),
    # url(r'^owner/(?P<pk>\d+)/delete/$', views.OwnerDelete.as_view(), name='ownerdelete'),

    # /petclinic/animal
    path('animal', views.AnimalView.as_view(), name='animals'),

    # /petclinic/animal/7
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name='animal'),

]
