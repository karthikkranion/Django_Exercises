from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Book
from .forms import BookForm

'''Class Based Views Implementation'''
class BookBaseView:
    model = Book
    form_class = BookForm
    context_object_name = 'book'

class BookCreateView(SuccessMessageMixin, BookBaseView, CreateView):
    template_name = 'book/book_form.html'
    success_message = 'Book created successfully'

    def get_success_url(self):
        return reverse('book-list')

class BookDetailView(BookBaseView, DetailView):
    template_name = 'book/book_detail.html'

class BookUpdateView(SuccessMessageMixin, BookBaseView, UpdateView):
    template_name = 'book/book_form.html'
    success_message = 'Book updated successfully'

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.pk})

class BookDeleteView(SuccessMessageMixin, BookBaseView, DeleteView):
    template_name = 'book/book_confirm_delete.html'
    success_message = 'Book deleted successfully'
    success_url = reverse_lazy('book-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        genre_filter = self.request.GET.get('genre', 'All')
        if genre_filter.lower() == 'all':
            return Book.objects.all().order_by('-created_at')
        return Book.objects.filter(genre__iexact=genre_filter).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = ['All', 'Fiction', 'Non-Fiction', 'History', 'Art', 'Science']
        context['current_genre'] = self.request.GET.get('genre', 'All')
        return context  
    

'''Function Based Views - Previous Implementation'''    
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Book
# from .forms import BookForm

# # ✅ Book List with Genre Filter
# def book_list(request):
#     genre_filter = request.GET.get('genre', 'All')
#     if genre_filter.lower() == 'all':
#         books = Book.objects.all().order_by('-created_at')
#     else:
#         books = Book.objects.filter(genre__iexact=genre_filter).order_by('-created_at')

#     genres = ['All', 'Fiction', 'Non-Fiction', 'History', 'Art', 'Science']
#     context = {
#         'books': books,
#         'genres': genres,
#         'current_genre': genre_filter,
#     }
#     return render(request, 'book/book_list.html', context)

# # ✅ Book Create
# def book_create(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book created successfully')
#             return redirect('book-list')
#     else:
#         form = BookForm()
#     return render(request, 'book/book_form.html', {'form': form})

# # ✅ Book Detail
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'book/book_detail.html', {'book': book})

# # ✅ Book Update
# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book updated successfully')
#             return redirect('book-detail', pk=book.pk)
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'book/book_form.html', {'form': form})

# # ✅ Book Delete with Confirmation
# def book_delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         messages.success(request, 'Book deleted successfully')
#         return redirect('book-list')
#     return render(request, 'book/book_confirm_delete.html', {'book': book})