from django.shortcuts import render, redirect
from . models import Customer
from .forms import CustomerForm
def show_customer(request):
    context={
        'customers':Customer.objects.all()
    }
    return render(request,'customer/show_customer.html',context)


def add_new_customer(request):
    form=CustomerForm()
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('customer:show_customer')

    return render(request,'customer/customer_register.html',{'form':form})


def remove_cutomer(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('customer:show_customer')