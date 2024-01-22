from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(name='Steak', price=15, menu_item_description='93percent lean beef steak')

        self.assertEqual(str(menu), 'Steak : 93percent lean beef steak')

        self.assertEqual(menu.name, 'Steak')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.menu_item_description, '93percent lean beef steak')