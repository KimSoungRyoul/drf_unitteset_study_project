# Create your models here.
from datetime import datetime
from enum import Enum

from django.db import models
from django_extensions.db import fields as extensions_field
from django_extensions.db.models import TimeStampedModel

from account.models import Customer
from cart.models import Cart
from product.models import Product


class ShippingStatus(Enum):
    payment_complete = '결제 완료'
    product_prepare = '상품 준비중'
    shipping_product = '상품 배송중'
    shipping_complete = '배송 완료'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Order(TimeStampedModel):
    total_price: int = models.PositiveIntegerField(help_text='주문된 상품들의 총 가격', null=False)

    owner: Customer = models.ForeignKey(Customer, help_text='주문을 소유한 회원', null=False, on_delete=models.CASCADE)

    shipping_address: str = models.CharField(max_length=256, null=False)
    shipping_message: str = models.CharField(max_length=128, null=True)

    contact_phone_num: str = models.CharField(max_length=64, null=False)


class ShippingInfo(models.Model):
    status: ShippingStatus = models.CharField(null=False, max_length=32, choices=ShippingStatus.choices())
    date: datetime = extensions_field.CreationDateTimeField()


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    owned_cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    owned_order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    amount = models.PositiveIntegerField(default=1)
