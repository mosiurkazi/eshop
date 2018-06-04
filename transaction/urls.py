from django.urls import path
from .views import buy_status, sell_status

urlpatterns = [

    path('today-buy-status/', buy_status, name='today-buy-status'),
    path('today-sell-status/', sell_status, name='today-sell-status'),


]
