from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserCreationForm,MyUserLoginForm
from .models import MyUser


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect('main:index')
    form = UserCreationForm()
    return render(request, 'account/register.html', {'form':form, 'error':form.errors})


def user_logout(request):
    logout(request)
    return redirect('main:index')


def user_login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user:
            login(request,user)
            return redirect('main:index')
    else:
        form=MyUserLoginForm()
        return render(request,'account/register.html',{'form':form})
