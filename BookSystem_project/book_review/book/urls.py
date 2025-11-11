from django.urls import path
from book.views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("create/", BookCreateView.as_view(), name="book-create"),
    path("detail/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("detail/<int:pk>/edit/", BookUpdateView.as_view(), name="book-update"),
    path("detail/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]