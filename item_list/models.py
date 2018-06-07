from django.db import models

# Create your models here.

class buyManager(models.Manager):
    def is_active(self):
        item = ItemList.objects.filter(is_active=True)
        return item

class ItemList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    objects = buyManager()

    def __str__(self):

        return self.name
