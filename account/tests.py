# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory


class TestSignUpCustomerAPI(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_superuser(username='root', password='django_password', email='')

    def test_signup_api(self):
        response = self.client.post(reverse('customer-list'),
                                    {
                                        "username": "sky53674",
                                        "password": "django_password1",
                                        "first_name": "string",
                                        "last_name": "string",
                                        "email": "user@example.com",
                                        "phone_num": "string",
                                        "nickname": "string"
                                    },
                                    )
        # force_authenticate(request, user=self.user)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
