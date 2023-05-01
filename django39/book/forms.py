from django import forms
from .models import Book
from .models import PublishingHouse

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price', 'publishing_house',)

class PublishingHouseForm(forms.ModelForm):

    class Meta:
        model = PublishingHouse
        fields = ('name', 'rating', )
