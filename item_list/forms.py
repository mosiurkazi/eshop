from django import forms
from .models import ItemList

class ItemListForm(forms.ModelForm):
    class Meta:
        model = ItemList
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
