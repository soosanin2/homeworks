from django.contrib import admin

from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):

    list_display = ('id', 'user_id', 'book_id', 'date')
    ordering = ('id', )


