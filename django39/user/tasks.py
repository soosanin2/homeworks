
from celery import shared_task
from .models import User
from purchase.models import Purchase

@shared_task
def my_task():
    users = User.objects.filter(age__gte=25)
    print(f'old user {users.count()}')



@shared_task(bind=False)
def count_user_purchases(user_id):
    user = User.objects.filter(id=user_id).first()
    purchase = Purchase.objects.filter(user_id=user.id)
    print(f'{user.first_name} {user.last_name} has {purchase.count()} purchases')


@shared_task
def all_users():
    users = User.objects.count()
    print(f'Number of all users: {users}')

