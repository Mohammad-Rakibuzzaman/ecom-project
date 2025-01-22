from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

# Home page: Display all products
def product_list(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'orders/product_list.html', {'products': products})

# Product detail page

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# Order placement page: Handles product order form
# def order_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)  # Retrieve the product
#     delivery_charge = None
#     total_price = product.price  # Default total price (base price)

#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.product = product

#             # Calculate delivery charge
#             area = form.cleaned_data['area']
#             delivery_charge = 70 if area == "inside" else 130

#             # Calculate total price
#             quantity = form.cleaned_data['quantity']
#             total_price = product.price * quantity + delivery_charge

#             # Save the order
#             order.delivery_charge = delivery_charge
#             order.total_price = total_price
#             order.save()
#             return redirect('success_page')
#     else:
#         form = OrderForm()

#     return render(request, 'orders/assets/order_form.html', {
#         'product': product,
#         'form': form,
#         'delivery_charge': delivery_charge,
#         'total_price': total_price,
#     })

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
    return render(request, 'orders/assets/order_form.html', {'form': form, 'product': product})

# Success page after order is placed
def success_page(request):
    return render(request, 'orders/assets/success.html')
