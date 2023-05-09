from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import PurchaseListView, PurchaseView
from .views import PurchaseViewSet


urlpatterns = [


]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls

