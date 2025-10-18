from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
# Create your models here.

def validate_pin(value):
    if len(str(value))!=6:
        raise ValidationError("Pin code must be 6 digits")


#to save list in database give two timmes full name 
state_choices=[
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
]
class Profile(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    pin=models.PositiveIntegerField(validators=[validate_pin],help_text="Enter 6 digit pin code")
    state=models.CharField(choices=state_choices,max_length=50)
    mobile=models.CharField(max_length=15,validators=[validators.RegexValidator(r'^\d{10}$')],help_text="Enter 10 digit mobile number")
    email=models.EmailField(max_length=100)
    job_city=models.CharField(max_length=50)    
    profile_image=models.ImageField(upload_to='profile_images/',blank=True,null=True)
    file=models.FileField(upload_to='documents/',blank=True,null=True)
    
    def __str__(self):
        return self.name