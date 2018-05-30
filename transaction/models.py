from django.db import models
from item_list.models import ItemList

# Create your models here.
class TransactionSystem(models.Model):
    item = models.ForeignKey(ItemList, on_delete=None)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.item.name
