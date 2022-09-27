from django.test import TestCase, tag
from django.urls import reverse
from main.models import Canteen


class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class CanteenTestCase(TestCase):
    def test_canteen_model(self):
        canteen = Canteen.objects.create(
            name="Canteen 1", address="Jl. Canteen 1", description="Canteen 1"
        )
        self.assertEqual(canteen.name, "Canteen 1")
        self.assertEqual(canteen.address, "Jl. Canteen 1")
        self.assertEqual(canteen.description, "Canteen 1")
        self.assertEqual(canteen.image, None)
        self.assertIsNotNone(canteen.date_joined)
        self.assertIsNotNone(canteen.date_updated)
        self.assertEqual(canteen.__str__(), "Canteen 1")

    def test_canteen_serializer(self):
        pass

    def test_canteen_view(self):
        pass

    def test_canteen_url(self):
        pass
