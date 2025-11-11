from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Book
from .forms import BookForm

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