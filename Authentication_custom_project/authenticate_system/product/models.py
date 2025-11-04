from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore

class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the product name")
    description = models.TextField(blank=True, null=True, help_text="Enter a description of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the product price")
    quantity = models.PositiveIntegerField(default=0, help_text="Number of items available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

