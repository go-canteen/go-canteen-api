from django.db import models
from user.models import Pengguna

# Create your models here.
class History(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)