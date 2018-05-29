from django.urls import path
from .views import add_item, show_item

urlpatterns = [

    path('add-item/', add_item, name='add_item'),
    path('show-items/', show_item, name='show-items'),


]
