from django.db import models
from item_list.models import ItemList

# Create your models here.
class InventorySystem(models.Model):
    item = models.OneToOneField(ItemList, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.item.name
