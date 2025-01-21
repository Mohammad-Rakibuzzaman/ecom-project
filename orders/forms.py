from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'quantity', 'delivery_option']
        labels = {
            'name': 'নাম',       # Bangla for "Name"
            'phone': 'ফোন',      # Bangla for "Phone"
            'address': 'ঠিকানা', # Bangla for "Address"
            'quantity': 'পরিমাণ নির্বাচন করুন',
            'delivery_option': 'এলাকা নির্বাচন করুন',
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
            'delivery_option': forms.Select(choices=[
                ('ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা', 'ডেলিভারি চার্জ ঢাকার ভিতরে ৭০ টাকা'),
                ('ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা', 'ডেলিভারি চার্জ ঢাকার বাহিরে ১৩০ টাকা'),
            ]),
        }
