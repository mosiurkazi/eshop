from django.urls import path
from .views import buy_status

urlpatterns = [

    path('today-buy_status/', buy_status, name='today-buy_status'),


]
