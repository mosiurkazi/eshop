from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def user_login(request):
    form = LoginForm()

    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data[ 'user_name']
            password = form.cleaned_data['password']

            print(user_name, password)

            user = authenticate(username=user_name, password=password)

            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'account/login.html',{'form':form, 'message':'User password not found'})


    return render(request, 'account/login.html', {'form':form})

def registration_form(request):
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = authenticate(user_name, password)

            login(request, user)
            return redirect('dashboard')

    return render(request, 'account/registration.html', {'form':form})

def user_logout(request):
    logout(request)

    return redirect('user-login')
