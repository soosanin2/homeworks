from django.http import JsonResponse
from .models import Book

def get_books(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        book_dict = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'price': book.price,
            'publishing_house_id': book.publishing_house_id.id
        }
        book_list.append(book_dict)
    return JsonResponse({'books': book_list})