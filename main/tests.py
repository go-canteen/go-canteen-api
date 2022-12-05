from django.test import TestCase, tag
from django.urls import reverse
from main.models import Canteen, CanteenBanner


class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class CanteenTestCase(TestCase):
    def setUp(self) -> None:
        self.canteen = Canteen.objects.create(
            name="Canteen 1", address="Jl. Canteen 1", description="Canteen 1"
        )
        self.canteen_banner_1 = CanteenBanner.objects.create(
            canteen=self.canteen, image="https://example.com/image.png"
        )
        self.canteen_banner_2 = CanteenBanner.objects.create(
            canteen=self.canteen, image="https://example.com/image.png"
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

    def test_canteen_banner_model(self):
        self.assertEqual(self.canteen_banner_1.canteen, self.canteen)
        self.assertEqual(self.canteen_banner_1.image, "https://example.com/image.png")
        self.assertEqual(self.canteen_banner_1.is_active, True)
        self.assertEqual(self.canteen_banner_1.on_click_url, None)
        self.assertIsNotNone(self.canteen_banner_1.date_joined)
        self.assertIsNotNone(self.canteen_banner_1.date_updated)
        self.assertEqual(
            self.canteen_banner_1.__str__(),
            "Canteen 1: " + str(self.canteen_banner_1.id),
        )

    def test_canteen_serializer(self):
        pass

    def test_canteen_view(self):
        pass

    def test_canteen_url(self):
        pass
