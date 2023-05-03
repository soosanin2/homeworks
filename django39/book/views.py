
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Book, PublishingHouse

from .serializers import BookSerializer, PublishingHouseSerializer
#
# class BookListView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class PublishingHouseListView(ListCreateAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer
#
# class PublishingHouseView(RetrieveUpdateDestroyAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublishingHouseViewSet(ModelViewSet):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingHouseSerializer
