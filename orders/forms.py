from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
        labels = {
            'name': 'নাম',       # Bangla for "Name"
            'phone': 'ফোন',      # Bangla for "Phone"
            'address': 'ঠিকানা', # Bangla for "Address"
        }
        # help_texts = {
        #     'name': 'আপনার পূর্ণ নাম লিখুন।',       # Example help text
        #     'phone': 'আপনার মোবাইল নাম্বার লিখুন।',
        #     'address': 'আপনার বর্তমান ঠিকানা লিখুন।',
        # }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'আপনার পূর্ণ নাম লিখুন'}),
            'phone': forms.TextInput(attrs={'placeholder': 'আপনার মোবাইল নাম্বার'}),
            'address': forms.TextInput(attrs={'placeholder': 'আপনার বর্তমান ঠিকানা'}),
        }
