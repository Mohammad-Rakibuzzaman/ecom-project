from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'orders/product_list.html', {'products': products})

def order_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('success_page')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'product': product})

def success_page(request):
    return render(request, 'orders/success.html')
