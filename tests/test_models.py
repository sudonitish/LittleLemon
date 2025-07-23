from django.test import TestCase
from littlelemon.restaurant.models import MenuTable


class MenuTableTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(Title="IceCream", Price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
