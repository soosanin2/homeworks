from django.urls import path
from .views import get_books, OllBooksList, IdBook, CreateBook

urlpatterns = [
    path('', get_books, name='get_books'),
    path('list', OllBooksList.as_view(), name='book-list'),
    path('list/<book_id>', IdBook.as_view(), name='id-book-list'),
    path('create/', CreateBook.as_view(), name='create-user'),
]