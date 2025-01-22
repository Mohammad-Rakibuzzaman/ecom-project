from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Home page to list products
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Product detail
    
    path('order/<int:pk>/', views.order_product, name='order_product'),  # Order placement
    path('success/', views.success_page, name='success_page'),  # Success page
]
