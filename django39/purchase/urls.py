from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import PurchaseListView, PurchaseView
from .views import PurchaseViewSet


urlpatterns = [
    # path('', PurchaseListView.as_view(), name='purchase-list'),
    # path('<int:pk>', PurchaseView.as_view(), name='purchase-main')
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls

