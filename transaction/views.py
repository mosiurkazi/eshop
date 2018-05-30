from django.shortcuts import render
from .models import TransactionSystem
import datetime

# Create your views here.
def buy_status(request):

    transaction_list = TransactionSystem.objects.filter(status='buy')
    
    return render(request, 'transaction/today_buy_status.html', {'transaction_list':transaction_list})
