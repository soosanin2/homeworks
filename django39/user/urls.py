from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import UserListView, UserView
from .views import UserViewSet

urlpatterns = [
    # path('', UserListView.as_view(), name='user-list'),
    # path('<int:pk>', UserView.as_view(), name='user-main')
]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
