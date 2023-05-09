from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import UserListView, UserView
from .views import UserViewSet

urlpatterns = [

]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
