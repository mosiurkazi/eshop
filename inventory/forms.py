from .models import InventorySystem
from django import forms
from item_list.models import ItemList

class InventoryBuyForm(forms.Form):

    item = forms.ModelChoiceField(queryset=ItemList.objects.is_active(), widget=forms.Select(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget)

class InventorySellForm(forms.Form):

    item = forms.ModelChoiceField(queryset=InventorySystem.objects.filter(quantity__gt=0), widget=forms.Select(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget)
