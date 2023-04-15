from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_items = [
            Menu.objects.create(Title='Pizza', Price=10.99, Inventory=100),
            Menu.objects.create(Title='Burger', Price=5.99, Inventory=50),
            Menu.objects.create(Title='Pasta', Price=12.99, Inventory=75),
        ]
        self.user = User.objects.create_user(
            username='testuser2', password='testpass')

    def test_getall(self):
        url = reverse('menu-items')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        expected_data = MenuSerializer(self.menu_items, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
