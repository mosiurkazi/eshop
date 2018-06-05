from django.urls import path
from .views import add_item, show_item, edit_item, dashboard_view, delete_item, home

urlpatterns = [


    path('home/', home, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('add-item/', add_item, name='add_item'),
    path('item-list/', show_item, name='item-list'),
    path('edit-items/<int:id>', edit_item, name='edit-items'),
    path('delete_item/<int:id>', delete_item, name='delete_item'),



]
