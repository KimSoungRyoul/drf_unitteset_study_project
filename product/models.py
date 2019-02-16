# Create your models here.

from django.db import models
from django_extensions.db.models import TimeStampedModel

from account.models import Marketer


class Product(TimeStampedModel):
    name: str = models.CharField(max_length=256, null=False)
    price: int = models.PositiveIntegerField()

    descriptions = models.TextField()

    marketer = models.ForeignKey(Marketer, on_delete=models.CASCADE, null=False)
