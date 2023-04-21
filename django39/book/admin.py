from django.contrib import admin
from .models import Book, PublishingHouse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price', 'publishing_house')
    ordering = ('id', )


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')
    ordering = ('id', )

