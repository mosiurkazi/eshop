from django.urls import path
from .views import inventory_view

urlpatterns = [

    path('inventory-form/', inventory_view, name='inventory-form'),

]
