from django.test import  TestCase, tag
from django.urls import reverse
from models import Order

class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class OrderTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            user="User 1", merchant="Merchant 1", content="Nasi Goreng"
        )
        return super().setUp()

def test_canteen_model(self):
    self.assertEqual(self.order.name, "User 1")
    self.assertEqual(self.order.merchant, "Merchant 1")
    self.assertEqual(self.order.content, "Nasi Goreng")
    self.assertIsNotNone(self.order.date)
