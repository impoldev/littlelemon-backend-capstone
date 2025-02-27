from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status

class MenuViewTest(TestCase):
  def setUp(self):
    Menu.objects.create(title='Pizza', price=50, inventory=200)
    Menu.objects.create(title='IceCream', price=80, inventory=100)
    Menu.objects.create(title='Hamburguer', price=70, inventory=120)

  def test_get_all(self):
    url = reverse('menu-items')
    response = self.client.get(url)

    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serializer.data)
  

