from django.urls import path
from .views import get_books, OllBooksList, IdBook, CreateBook, OllPublishingHouse, IdPublishingHouse, CreatePublishingHouse

urlpatterns = [
    path('', get_books, name='get_books'),
    path('list', OllBooksList.as_view(), name='book-list'),
    path('list/<book_id>', IdBook.as_view(), name='id-book-list'),
    path('create/', CreateBook.as_view(), name='create-user'),
    path('publishing_house/list', OllPublishingHouse.as_view(), name='publishing_house-list'),
    path('publishing_house/list/<publishing_house_id>', IdPublishingHouse.as_view(), name='id-publishing_house-list'),
    path('publishing_house/create', CreatePublishingHouse.as_view(), name='create-publishing_house'),
]