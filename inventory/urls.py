from django.urls import path
from .views import inventory_buy_form, inventory_sell_form, inventory_list_view

urlpatterns = [

    path('inventory-buy-form/', inventory_buy_form, name='inventory-buy-form'),
    path('inventory-sell-form/', inventory_sell_form, name='inventory-sell-form'),
    path('inventory-list-view/', inventory_list_view, name='inventory-list-view'),


]
