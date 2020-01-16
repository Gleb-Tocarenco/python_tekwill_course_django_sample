from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_app.models import FancyCat


class ListApiTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('fancy_cats_list')

        FancyCat.objects.create(name='Alex', age=2)
        FancyCat.objects.create(name='Oscar', age=1)

    def test_get_method(self):
        reponse = self.client.get(self.url)

        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertEqual(reponse.data, [
            {'name': 'Alex', 'id': 1},
            {'name': 'Oscar', 'id': 2},
        ])

    def test_post_method(self):
        data = {'name': 'Mary'}
        user = User.objects.create_superuser(
            username='username', 
            email='test@email.com',
            password='1234',
            )
        self.client.force_login(user)
        reponse = self.client.post(self.url, data)
        self.assertEqual(reponse.status_code, status.HTTP_201_CREATED)
        self.assertEqual(reponse.data['id'], 3)
        self.assertEqual(reponse.data['name'], 'Mary')
        self.assertEqual(FancyCat.objects.count(), 3)

    def test_not_authenticated(self):
        data = {'name': 'Mary'}
        reponse = self.client.post(self.url, data)
        self.assertEqual(reponse.status_code, status.HTTP_403_FORBIDDEN)

    def test_bad_request(self):
        data = {}
        user = User.objects.create_superuser(
            username='username', 
            email='test@email.com',
            password='1234',
            )
        self.client.force_login(user)
        reponse = self.client.post(self.url, data)
        self.assertEqual(reponse.status_code, status.HTTP_400_BAD_REQUEST)


class DetailApiTestCase(TestCase):

    def setUp(self):
        self.cat = FancyCat.objects.create(name='Alex', age=2)
        self.client = Client()
        self.url = reverse('fancy_cats_detail', args=(self.cat.id, ))

    
    def test_put_url(self):
        user = User.objects.create_superuser(
            username='username', 
            email='test@email.com',
            password='1234',
            )
        self.client.force_login(user)
        response = self.client.put(self.url, {'name': 'Oscar'}, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
