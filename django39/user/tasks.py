
from celery import shared_task
from .models import User
from purchase.models import Purchase

@shared_task
def my_task():
    users = User.objects.filter(age__gte=25)
    print(f'old user {users.count()}')


@shared_task()
def count_user_purchases(user_id):
    user = User.objects.get(id=user_id)
    print(f'{user.first_name} {user.last_name} has {user.purchases.count()} purchases')


@shared_task
def all_users():
    users = User.objects.count()
    print(f'Number of all users: {users}')

