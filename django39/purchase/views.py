import django_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import filters

from .models import Purchase

from .serializers import PurchaseSerializer


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'book_id': ['exact', 'in'],
            'user_id': ['exact', 'in'],
            'date': ['year', 'month', 'day']
        }


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PurchaseFilter
    search_fields = ['book_id', 'user_id']
    ordering_fields = ['date']