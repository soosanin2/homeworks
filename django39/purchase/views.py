from django.http import JsonResponse
from .models import Purchase

def get_purchases(request):
    purchases = Purchase.objects.all()
    purchase_list = []
    for purchase in purchases:
        purchase_dict = {
            'id': purchase.id,
            'user_id': purchase.user_id.id,
            'book_id': purchase.book_id.id,
            'date': purchase.date
        }
        purchase_list.append(purchase_dict)
    return JsonResponse({'purchases': purchase_list})