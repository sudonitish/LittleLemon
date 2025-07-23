from django.test import TestCase
from littlelemon.restaurant.models import MenuTable
from littlelemon.restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        MenuTable.objects.create(Title="IceCream", Price=80, inventory=100)
        MenuTable.objects.create(Title="Cake", Price=150, inventory=50)

    def test_getall(self):
        items = MenuTable.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(
            serializer.data,
            [
                {
                    "id": items[0].id,
                    "Title": "IceCream",
                    "Price": "80.00",
                    "inventory": 100,
                },
                {
                    "id": items[1].id,
                    "Title": "Cake",
                    "Price": "150.00",
                    "inventory": 50,
                },
            ],
        )
