from django.db import models

# Create your models here.
class TransactionSystem(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=100)
    date = models.DateTimeField()
