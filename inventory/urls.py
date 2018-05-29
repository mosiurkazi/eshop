from django.urls import path
from .views import inventory_view, inventory_sell_view

urlpatterns = [

    path('inventory-form/', inventory_view, name='inventory-form'),
    path('sell-form/', inventory_sell_view, name='sell-form'),

]
