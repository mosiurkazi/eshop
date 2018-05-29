from django.shortcuts import render
from .models import InventorySystem
from .forms import InventoryForm


# Create your views here.

def inventory_view(request):
    form = InventoryForm()

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():

            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']

            print(item, quantity, price)

            return render(request, 'inventory/inventory.html', {'form':form})

    return render(request, 'inventory/inventory.html', {'form':form})
