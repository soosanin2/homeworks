from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import Book, PublishingHouse
from .forms import BookForm, PublishingHouseForm


class OllPublishingHouse(ListView):
    model = PublishingHouse
    template_name = 'book/publishing_house_list.html'

class IdPublishingHouse(DetailView):
    model = PublishingHouse
    pk_url_kwarg = 'publishing_house_id'
    template_name = 'book/publishing_house_detail.html'

class CreatePublishingHouse(CreateView):
    model = PublishingHouse
    form_class = PublishingHouseForm
    template_name = 'book/publishing_house_form.html'
    success_url = reverse_lazy('publishing_house-list')



class OllBooksList(ListView):
    model = Book

class IdBook(DetailView):
    model = Book
    pk_url_kwarg = 'book_id'

class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('book-list')


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