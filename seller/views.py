from django.shortcuts import render, redirect

from .forms import SellerForm
from . models import Seller
# Create your views here.


def seller_list(request):
    sellers = Seller.objects.all()
    return render(request,'seller/seller_list.html',{'sellers':sellers})


def add_new_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller:seller-list')
    form = SellerForm()
    return render(request,'seller/seller_register.html',{'form':form})


def delete_seller(request,pk):
    seller = Seller.objects.get(pk=pk)
    seller.delete()
    return redirect('seller:seller-list')