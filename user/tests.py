from django.test import TestCase
from .models import Pengguna


class PenggunaTestCase(TestCase):
    def setUp(self):
        self.pengguna = Pengguna.objects.create(
            username="admin", password="admin", email="admin@gocanteen.com"
        )

    def test_pengguna(self):
        self.assertEqual(self.pengguna.username, "admin")
        self.assertEqual(self.pengguna.email, "admin@gocanteen.com")
