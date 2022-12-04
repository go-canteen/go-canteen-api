from django.test import TestCase
from .models import History
from user.models import Pengguna

class PenggunaTestCase(TestCase):
    def setUp(self):
        self.pengguna = Pengguna.objects.create(
            username="admin", password="admin", email="admin@gocanteen.com"
        )
        self.history = History.objects.create(
            user=self.pengguna
        )

    def test_history(self):
        self.assertEqual(self.pengguna, self.history.user)
        self.assertEqual(self.history.user.id, 1)
        self.assertEqual(self.history.user.username, "admin")
        self.assertEqual(self.history.user.email, "admin@gocanteen.com")
