from django.urls import path # type: ignore
from book import views

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("create/", views.book_create, name="book-create"),
    path("detail/<int:pk>/", views.book_detail, name="book-detail"),
    path("detail/<int:pk>/edit/", views.book_update, name="book-update"),
    path("detail/<int:pk>/delete/", views.book_delete, name="book-delete"),
]
