
import django_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import filters
from .models import Book, PublishingHouse
from rest_framework.pagination import PageNumberPagination
from .serializers import BookSerializer, PublishingHouseSerializer



class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'price': ['gte', 'lte', 'gt', 'lt', 'exact']
        }

class PublishingHouseFilter(django_filters.FilterSet):
    class Meta:
        model = PublishingHouse
        fields = {
            'name': ['contains'],
            'rating': ['gte', 'lte', 'gt', 'lt', 'exact']
        }



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['price']


class PublishingHouseViewSet(ModelViewSet):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingHouseSerializer

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PublishingHouseFilter
    search_fields = ['name']
    ordering_fields = ['rating']
