from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import User
from .forms import UserForm

class OllUsersList(ListView):
    template_name = 'user/my_user_list.html'
    model = User

class IdUser(DetailView):
    model = User
    pk_url_kwarg = 'user_id'

class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user-list')





