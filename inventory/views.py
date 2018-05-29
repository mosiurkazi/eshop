from django.shortcuts import render
from .models import InventorySystem
from .forms import InventoryForm
from transaction.models import TransactionSystem
import datetime



# Create your views here.

def inventory_view(request):
    form = InventoryForm()

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():

            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']

            try:
                a = InventorySystem.objects.get(item=item)
                a.quantity = a.quantity + quantity
                a.save()

            except:

                InventorySystem.objects.create(
                            item=item,
                            quantity=quantity,
                            price=price
                            )


            TransactionSystem.objects.create(
                        item=item,
                        quantity=quantity,
                        price=price,
                        status='yes',
                        date=datetime.datetime.now()
                        )
            return render(request, 'inventory/inventory.html', {'form':form})

    return render(request, 'inventory/inventory.html', {'form':form})

def inventory_sell_view(request):
    sell_form = InventoryForm()

    if request.method == 'POST':
        sell_form = InventoryForm(request.POST)
        if sell_form.is_valid():

            item = sell_form.cleaned_data['item']
            quantity = sell_form.cleaned_data['quantity']
            price = sell_form.cleaned_data['price']


            b = InventorySystem.objects.get(item=item)
            b.quantity = b.quantity - quantity
            b.save()


            TransactionSystem.objects.create(
                        item=item,
                        quantity=quantity,
                        price=price,
                        status='yes',
                        date=datetime.datetime.now()
                        )
            return render(request, 'inventory/sell_inventory.html', {'sell_form':sell_form})

    return render(request, 'inventory/sell_inventory.html', {'sell_form':sell_form})
