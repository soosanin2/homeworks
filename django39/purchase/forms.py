from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):


    class Meta:
        model = Purchase
        fields = ('date', 'book', 'user', )

