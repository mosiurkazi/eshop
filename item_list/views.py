from django.shortcuts import render,redirect
from .models import ItemList
from .forms import ItemListForm

# Create your views here.

def add_item(request):

    form = ItemListForm()

    if request.method == 'POST':
        form = ItemListForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('show-items')

    else:
        form = ItemListForm()

    return render(request, 'item_list/item_list.html', {'form':form})

def show_item(request):

    item_list = ItemList.objects.all()

    return render(request, 'item_list/add_items.html', {'item_list':item_list})
