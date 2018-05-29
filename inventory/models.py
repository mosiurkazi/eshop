from django.db import models
from item_list.models import ItemList

# Create your models here.
class InventorySystem(models.Model):
    Item = models.ForeignKey(ItemList, on_delete=None)
    quantity = models.IntegerField()
    price = models.IntegerField()
