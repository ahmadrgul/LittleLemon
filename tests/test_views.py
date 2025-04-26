from django.test import TestCase
from Restaurant.models import MenuItem
from django.urls import reverse

class MenuItemViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="biryani", price=230, inventory=20)
    
    # def test_getall(self):
    #     url = reverse('menu-items-all')
    #     response = self.client.get(url)