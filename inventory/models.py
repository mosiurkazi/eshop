from django.db import models

# Create your models here.
class InventorySystem(models.Model):
    Item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
