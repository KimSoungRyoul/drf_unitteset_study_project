# Create your models here.
from django.contrib.auth import models as auth_models
from django.db import models


class Customer(auth_models.User):
    nickname = models.CharField(help_text='회원 닉네임', null=False, max_length=50)

    phone_num = models.CharField(null=False, max_length=50)

    mileage = models.PositiveIntegerField(default=0)


class Marketer(auth_models.User):
    business_registration_number = models.CharField(max_length=128, unique=True)

    company_name = models.CharField(max_length=128, null=True)
