from django.urls import path
from .views import inventory_view, inventory_sell_view, inventory_list_view

urlpatterns = [

    path('inventory-form/', inventory_view, name='inventory-form'),
    path('sell-form/', inventory_sell_view, name='sell-form'),
    path('inventory-list-view/', inventory_list_view, name='inventory-list-view'),


]
