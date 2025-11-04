from django import forms # type: ignore
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','price']
       
       