# Create your models here.
from datetime import datetime

from django.db import models
from django_extensions.db import fields as extensions_field

from account.models import Customer


class Cart(models.Model):
    owner: Customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=False)

    updated_date: datetime = extensions_field.ModificationDateTimeField()

    total_price: int = models.PositiveIntegerField()
