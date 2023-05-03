
from django.urls import path


from rest_framework.routers import SimpleRouter
# from .views import BookListView, PublishingHouseListView, BookView, PublishingHouseView
from .views import BookViewSet, PublishingHouseViewSet


urlpatterns = [
    # path('', BookListView.as_view(), name='book-list'),
    # path('<int:pk>', BookView.as_view(), name='book-main'),
    # path('house', PublishingHouseListView.as_view(), name='publishing_house-list'),
    # path('<int:pk>', PublishingHouseView.as_view(), name='publishing_house-main')
]

router = SimpleRouter()
router.register('', BookViewSet)
router.register('/house', PublishingHouseViewSet)

urlpatterns += router.urls


