from .models import InventorySystem
from django import forms
from item_list.models import ItemList

class InventoryForm(forms.Form):

    item = forms.ModelChoiceField(queryset=ItemList.objects.all())
    quantity = forms.IntegerField()
    price = forms.IntegerField()
