from django.db import models
from user.models import User
from book.models import Book

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f"User Id:{self.user.id}   book id:{self.book.id}   date:{self.date}"