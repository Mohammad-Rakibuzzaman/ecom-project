from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order/<int:pk>/', views.order_product, name='order_product'),
  
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Match the ID

    path('success/', views.success_page, name='success_page'),
]
