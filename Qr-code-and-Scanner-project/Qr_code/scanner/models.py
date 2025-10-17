from django.db import models

# Create your models here.
class Qrcode(models.Model):
     data =models.CharField(max_length=200)
     mobile_number = models.CharField(max_length=15)
     upi_id = models.CharField(max_length=100,default='')

     def __str__(self):
         return  f"{self.data}-{self.mobile_number}"