from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'genre',
            'isbn',
            'publication_date',
            
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write a short description of the book'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 13-digit ISBN number'
            }),
            'publication_date':forms.DateInput(attrs={'class':'form-control',
                                                      'type':'date'
                                                      }),
        }