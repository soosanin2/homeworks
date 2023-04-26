from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import Purchase
from .forms import PurchaseForm


class OllPurchasesList(ListView):
    model = Purchase


class IdPurchase(DetailView):
    model = Purchase
    pk_url_kwarg = 'purchase_id'


class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/purchase_form.html'
    success_url = reverse_lazy('purchase-list')


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