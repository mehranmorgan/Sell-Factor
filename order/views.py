from django.shortcuts import render, redirect
from customer.models import Customer
from order.models import Order, OrderItem
from product.models import Product
from seller.models import Seller


def order_register(request):
    customers = Customer.objects.all()
    sellers = Seller.objects.all()
    context = {
        'customers': customers,
        'sellers': sellers,
    }
    customer_id = str(request.GET.get('customer_id'))
    seller_id = str(request.GET.get('seller_id'))
    if customer_id.isdigit() and seller_id.isdigit():
        customer = Customer.objects.get(id=customer_id)
        seller = Seller.objects.get(id=seller_id)
        new_order = Order.objects.create(customer=customer,seller=seller )
    return render(request, 'order/order_register.html', context)


def order_remove(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('order:order_register')


def order_item(request, id):
    print('hello')
    products = Product.objects.all()
    order = Order.objects.get(id=id)
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
    return render(request, 'order/item_register.html', {'products': products, 'order': order})


def add_item(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        product_id = request.POST.get('id')
        qty = request.POST.get('qty')
        print(order_id, product_id, qty)
        if order_id and product_id and qty:
            order = Order.objects.get(id=order_id)
            product = Product.objects.get(id=product_id)
            new_item = OrderItem.objects.create(order=order, product=product, qty=qty)
            print('ok')
        return redirect('order:order_item', id=order_id)


def show_item_list(request, id):
    order = Order.objects.get(id=id)
    items = order.items.all()
    return render(request, 'order/show_item_list.html', {'items': items,'order_id':id})


def delete_item_list(request,order_id,product_id):
    order=Order.objects.get(id=order_id)
    item=order.items.get(id=product_id)
    item.delete()
    return redirect('order:show_item_list', id=order_id)


def factor(request,id):
    order = Order.objects.get(id=id)
    items = order.items.all()
    return render(request,'order/factor.html',{'order':order,'items':items})


def show_item_list_no_price(request,id):
    order = Order.objects.get(id=id)
    items = order.items.all()
    return render(request, 'order/show_item_list_no_price.html', {'items': items,'order_id':id})


def factor_no_price(request,id):
    order = Order.objects.get(id=id)
    items = order.items.all()
    return render(request,'order/factor_no_price.html',{'order':order,'items':items})