from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     image = models.ImageField(upload_to='products/')
    
#     def __str__(self):
#         return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # Save images in media/products/
    
    def __str__(self):
        return self.name


# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, verbose_name="নাম")       # Bangla for "Name"
#     phone = models.CharField(max_length=15, verbose_name="ফোন")      # Bangla for "Phone"
#     address = models.CharField(max_length=100, verbose_name="ঠিকানা")               # Bangla for "Address")
#     status = models.CharField(max_length=50, default='Pending')
#     discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def total_price(self):
#         return max(self.product.price - self.discount, 0)

#     def __str__(self):
#         return f"Order #{self.id} - {self.product.name}"


# class Order(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     quantity = models.PositiveIntegerField()  # Ensure this field exists
#     delivery_option = models.CharField(  # Ensure this field exists
#         max_length=50,
#         choices=[
#             ('ঢাকার ভিতরে', 'ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা'),
#             ('ঢাকার বাহিরে', 'ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা'),
#         ]
#     )

#     def __str__(self):
#         return self.name


class Order(models.Model):
    product = models.CharField(max_length=255)  # Example field for product name
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled'),
        ],
        default='pending'
    )
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Example field for discount
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    # quantity = models.PositiveIntegerField(default=1)
    delivery_option = models.CharField(
        max_length=50,
        choices=[
            ('ঢাকার ভিতরে', 'ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা'),
            ('ঢাকার বাহিরে', 'ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা'),
        ],
        default='ঢাকার ভিতরে',
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name