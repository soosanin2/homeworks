
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Purchase

from .serializers import PurchaseSerializer


# class PurchaseListView(ListCreateAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#
# class PurchaseView(RetrieveUpdateDestroyAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer