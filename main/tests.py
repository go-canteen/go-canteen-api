from django.test import  TestCase, tag
from django.urls import reverse
from main.models import Canteen

class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class CanteenTestCase(TestCase):
    def setUp(self) -> None:
        self.canteen = Canteen.objects.create(
            name="Canteen 1", address="Jl. Canteen 1", description="Canteen 1"
        )
        return super().setUp()

def test_canteen_model(self):
        self.assertEqual(self.canteen.name, "Canteen 1")
        self.assertEqual(self.canteen.address, "Jl. Canteen 1")
        self.assertEqual(self.canteen.description, "Canteen 1")
        self.assertEqual(self.canteen.image, None)
        self.assertIsNotNone(self.canteen.date_joined)
        self.assertIsNotNone(self.canteen.date_updated)
        self.assertEqual(self.canteen.__str__(), "Canteen 1")