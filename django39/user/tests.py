
import random
import factory

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from user.models import User


class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)

    class Meta:
        model = User


class AdultUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(18, 100)

    class Meta:
        model = User


class YangUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 17)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()
        cls.adult_user = AdultUserFactory.create()
        cls.yang_user = YangUserFactory.create()

    def test_user(self):
        self.assertIsInstance(self.user, User)

    def test_user_age(self):
        self.assertIsNotNone(self.user.age)
        print(self.user)

    def test_adult_user(self):
        self.assertTrue(self.adult_user.is_adult())
        self.assertFalse(self.yang_user.is_adult())

# view tests

class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_get_user_list_option_one(self):
        response = self.client.get(f'/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('count'), 1)
        random_namber = random.randint(1, 10)
        for _ in range(random_namber):
            RandomUserFactory.create()
        response = self.client.get(f'/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('count'), random_namber + 1)

    def test_user_create_option_one(self):
        user_data = {
            'first_name': 'Createdtest',
            'last_name': 'Testcreated',
            'age': 1
        }
        response = self.client.post('/user/', data=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('first_name'), user_data.get('first_name'))

    def test_user_create_option_two(self):
        response = self.client.get(f'/user/{self.user.id}/')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.first_name, response.json().get('first_name'))
        self.assertEqual(self.user.last_name, response.json().get('last_name'))
        self.assertEqual(self.user.age, response.json().get('age'))

    def test_get_user_list_option_two(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('count'), 1)

    def test_get_user_detail(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), self.user.first_name)
        self.assertEqual(response.json().get('last_name'), self.user.last_name)
        self.assertEqual(response.json().get('age'), self.user.age)

    def test_delete_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
