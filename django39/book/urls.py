
from django.urls import path


from rest_framework.routers import SimpleRouter
# from .views import BookListView, PublishingHouseListView, BookView, PublishingHouseView
from .views import BookViewSet, PublishingHouseViewSet


urlpatterns = [

]

router = SimpleRouter()
router.register('', BookViewSet)
router.register('/house', PublishingHouseViewSet)

urlpatterns += router.urls


