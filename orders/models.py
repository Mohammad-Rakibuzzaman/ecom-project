from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # Save images in media/products/
    
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def total_price(self):
        return max(self.product.price - self.discount, 0)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"
