from django.db import models
from user.models import User


class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)

    class Meta:
        db_table = 'publishing_house'

    def __str__(self):
        return f" publishing house: {self.name} - rating: {self.rating}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=False)
    price = models.CharField(max_length=10)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"Title: {self.title}, author :{self.author}, date: {self.year}, price: {self.price}, publishing house: {self.publishing_house}"