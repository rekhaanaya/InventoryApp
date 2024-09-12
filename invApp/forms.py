from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        lables = {
            'product_id': 'Product ID',
            'name' : 'Name',
            'sku': 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier': 'Supplier',
        }

        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g 1', 'class':'form-control'}),
            'name': forms.NumberInput(attrs={'placeholder': 'shirt', 'class':'form-control'}),
            'sku': forms.NumberInput(attrs={'placeholder': 's12345', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': '19.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': '10', 'class':'form-control'}),
            'supplier': forms.NumberInput(attrs={'placeholder': 'ABC Corp', 'class':'form-control'}),





        }