from django.urls import path
from .views import OllUsersList, IdUser, CreateUser


urlpatterns = [
    path('list', OllUsersList.as_view(), name='user-list'),
    path('list/<user_id>', IdUser.as_view(), name='id-user-list'),
    path('create/', CreateUser.as_view(), name='create-user'),
]