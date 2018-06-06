from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ItemList
from .forms import ItemListForm

# Create your views here.

@login_required
def add_item(request):

    form = ItemListForm()

    if request.method == 'POST':
        form = ItemListForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('item-list')

    else:
        form = ItemListForm()

    return render(request, 'item_list/add_items.html', {'form':form})

@login_required
def show_item(request):

    item_list = ItemList.objects.all()

    return render(request, 'item_list/item_list.html', {'item_list':item_list})

@login_required
def edit_item(request, id):
    if request.method == 'POST':
        item = ItemList.objects.get(id=id)
        clause = ItemListForm(request.POST,instance=item)
        if clause.is_valid():
            clause.save()
            return redirect('item-list')
    else:
        item = ItemList.objects.get(id=id)
        clause = ItemListForm(instance=item)

    return render(request, 'item_list/edit_item.html',{'clause':clause})

@login_required
def delete_item(request, id):
    item = ItemList.objects.get(id=id)
    print('item',type(item))
    item.delete()
    return redirect('item-list')

@login_required
def dashboard_view(request):

    return render(request, 'dashboard.html')
@login_required
def home(request):

    return render(request, 'home.html')
