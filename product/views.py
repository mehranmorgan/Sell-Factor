from django.shortcuts import render, redirect

from .forms import ProductForm
from . models import Product
def show_product(request):
    products = Product.objects.all()
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
    context = {'products': products}
    return render(request, 'product/show_product.html', context)


def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # اصلاح نحوه ارسال داده‌ها
        if form.is_valid():
            form.save()
            return redirect('product:add_product')  # بهتره به لیست محصولات هدایت بشه
    context = {'form': form}
    return render(request, 'product/product_register.html', context)


def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product:show_product')