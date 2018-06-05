from .models import InventorySystem
from django import forms
from item_list.models import ItemList

class InventoryForm(forms.Form):

    item = forms.ModelChoiceField(queryset=ItemList.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    test = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget)
