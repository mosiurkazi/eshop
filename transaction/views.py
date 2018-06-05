from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TransactionSystem
import datetime

# Create your views here.
@login_required
def buy_status(request):

    transaction_list = TransactionSystem.objects.filter(date__date=datetime.date.today(), status='buy')

    return render(request, 'transaction/today_buy_status.html', {'transaction_list':transaction_list})

@login_required
def sell_status(request):

    transaction_list = TransactionSystem.objects.filter(date__date=datetime.date.today(), status='sell')

    return render(request, 'transaction/today_sell_status.html', {'transaction_list':transaction_list})
