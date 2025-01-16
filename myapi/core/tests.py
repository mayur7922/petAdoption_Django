from rest_framework.test import APITestCase #type: ignore
from rest_framework import status #type: ignore
from django.contrib.auth.models import User #type: ignore
from rest_framework.authtoken.models import Token #type: ignore

# for testing change the database url from settings.py to testdb

class AdminPetsAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='password')
        self.token = Token.objects.create(user=self.user)
        self.auth_header = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        self.pet_list_url = '/admin/pets/'
        self.pet_detail_url = '/admin/pets/5/'

    def test_get_pets(self):
        response = self.client.get(self.pet_list_url, **self.auth_header)

    def test_create_pet(self):
        data = {
            "type": "Bird",
            "breed": "New type",
            "age": 2,
            "isAdopted": False,
            "user_id": 0
        }
        response = self.client.post(self.pet_list_url, data, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], "Bird")
        self.assertEqual(response.data['breed'], "New type")
        self.assertEqual(response.data['age'], 2)
        self.assertEqual(response.data['isAdopted'], False)
        self.assertEqual(response.data['user_id'], 0)
