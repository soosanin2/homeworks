from django.urls import path
from .views import get_purchases, OllPurchasesList, IdPurchase, CreatePurchase




urlpatterns = [
    path('', get_purchases, name='get_purchases'),
    path('list', OllPurchasesList.as_view(), name='purchase-list'),
    path('list/<purchase_id>', IdPurchase.as_view(), name='id-purchase-list'),
    path('create/', CreatePurchase.as_view(), name='create-purchase'),
]