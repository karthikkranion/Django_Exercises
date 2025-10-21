from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    GENRE_CHOICES =[
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Sceince','Sceince'),
        ('Art','Art'),
        ('Technology','Technology'),
        ('History','History'),
        ('other','other')
    ]

    title=models.CharField(max_length=250)
    author=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    genre=models.CharField(max_length=20,choices=GENRE_CHOICES)
    isbn=models.CharField('ISBN',max_length=13,unique=True)
    publication_date=models.DateField()
    average_rating=models.DecimalField(max_digits=3,
                                       decimal_places=2,
                                       validators=[MinValueValidator(0)
                                                   ,MaxValueValidator(5)]
                                        ,default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return  self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    