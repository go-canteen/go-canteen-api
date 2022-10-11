from django.test import TestCase, tag
from django.urls import reverse
from main.models import Canteen, CanteenBanner
from rest_framework.test import APITestCase
from rest_framework import status
from main.serializers import CanteenSerializer
from main.views import CanteenList
import io
import json
from rest_framework.parsers import JSONParser

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

class CanteenAPITest(APITestCase):
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

    def test_get_canteen_list(self):
        url = reverse('canteens')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.resolver_match.func.view_class, CanteenList)
        
    def test_create_canteen(self):
        url = reverse('canteens')
        data = {"name" : "Canteen 2", "address" : "Jl. Canteen 2", "description" : "Canteen 2"}
        response = self.client.post(url, data, format = "json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Canteen.objects.count(), 2)
        self.assertEqual(Canteen.objects.get(name='Canteen 2').address, "Jl. Canteen 2")

    def test_get_canteen_detail(self):
        canteen_id = Canteen.objects.get().id
        url = reverse('canteen-detail', args=[canteen_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(canteen_id))
    
    def test_get_canteen_detail_not_found(self):
        response = self.client.get('/canteens/abcd')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_canteen_detail(self):
        canteen_id = Canteen.objects.get().id
        url = reverse('canteen-detail', args=[canteen_id])
        data = {"name" : "Canteen 2", "address" : "Jl. Canteen 2", "description" : "Canteen 2"}
        response = self.client.put(url, data, format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Canteen 2")

    def test_delete_canteen_detail(self):
        canteen_id = Canteen.objects.get().id
        url = reverse('canteen-detail', args=[canteen_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Canteen.objects.count(), 0)