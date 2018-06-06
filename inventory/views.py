from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import InventorySystem
from .forms import InventoryBuyForm, InventorySellForm
from transaction.models import TransactionSystem
import datetime




# Create your views here.
@login_required
def inventory_buy_form(request):
    form = InventoryBuyForm()

    if request.method == 'POST':
        form = InventoryBuyForm(request.POST)
        if form.is_valid():

            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']

            try:
                a = InventorySystem.objects.get(item=item)
                # update previous quantity
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
                        status='buy',
                        date=datetime.datetime.now()
                        )

            return redirect('inventory-list-view')
            # return render(request, 'inventory/inventory.html', {'form':form})

    return render(request, 'inventory/inventory_buy_form.html', {'form':form})

@login_required
def inventory_sell_form(request):
    sell_form = InventorySellForm()

    if request.method == 'POST':
        sell_form = InventorySellForm(request.POST)
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
                        status='sell',
                        date=datetime.datetime.now()
                        )
            return redirect('inventory-list-view')

    return render(request, 'inventory/inventory_sell_form.html', {'form':sell_form})

@login_required
def inventory_list_view(request):


    # inventoty_list = InventoryForm()
    #
    # if request.method == 'POST':
    #     inventoty_list = InventoryForm(request.POST)
    #     if inventoty_list.is_valid():
    #         inventoty_list.save()
            #
            # item = inventoty_list.cleaned_data['item']
            # quantity = inventoty_list.cleaned_data['quantity']
            # price = inventoty_list.cleaned_data['price']

    all_inventory = InventorySystem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'all_inventory':all_inventory})
