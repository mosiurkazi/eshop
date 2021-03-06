"""eshopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import inventory.urls as inventory_urls
import item_list.urls as item_list_urls
import transaction.urls as transaction_urls
import account.urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventories/', include(inventory_urls)),
    path('items/', include(item_list_urls)),
    path('transactions/', include(transaction_urls)),
    path('account/', include(account_urls)),
]
