from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
from django.contrib import messages
# Create your views here.

def book_create(request):
    if request.method == 'POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book created successfully')
            return redirect('book-list')
    else:
        form=BookForm()
    return  render(request,'book/book_form.html',{'form':form})

def book_list(request):
    genre_filter = request.GET.get('genre', 'all')  # get ?genre=fiction etc.
    
    if genre_filter == 'all':
        books = Book.objects.all().order_by('-created_at')
    else:
        books = Book.objects.filter(genre__iexact=genre_filter).order_by('-created_at')

    genres = ['All', 'Fiction', 'Non-Fiction', 'History', 'Art', 'Science']

    return render(request, 'book/book_list.html', {
        'books': books,
        'genres': genres,
        'current_genre': genre_filter,
    })


def book_detail(request,pk):
    book=Book.objects.get(pk=pk)
    return render(request,'book/book_detail.html',{'book':book})

def book_update(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method == 'POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated successfully')
            return redirect('book-detail',pk=book.pk)
    else:
        form=BookForm(instance=book)
    return  render(request,'book/book_form.html',{'form':form})
    
def book_delete(request,pk):
     book=Book.objects.get(pk=pk)
     book.delete()
     messages.success(request,'Book deleted successfully')
     return redirect('book-list')
     