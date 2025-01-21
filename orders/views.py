from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm




def product_detail(request, id):  # `id` must match the URL pattern
    product = get_object_or_404(Product, id=id)  # Fetch the product or return 404
    return render(request, 'product_detail.html', {'product': product})

def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()

    delivery_options = [
        ('ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা', 'ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা'),
        ('ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা', 'ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা'),
    ]
    return render(request, 'order_form.html', {
        'product': product,
        'form': form,
        'delivery_options': delivery_options,
    })






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
