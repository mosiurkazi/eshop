from django.contrib import admin
from .models import InventorySystem

# Register your models here.



class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price')

admin.site.register(InventorySystem, InventoryAdmin)
