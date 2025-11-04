from django.contrib import admin # type: ignore
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display =['name','price','description']
    
