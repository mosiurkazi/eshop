from django.db import models

# Create your models here.
class ItemList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
