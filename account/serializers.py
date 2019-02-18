from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from account.models import Customer


class CustomerInfoSerializer(ModelSerializer):
    username = serializers.CharField(help_text='회원의 아이디')

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'nickname', 'phone_num', 'mileage']


class SignUpFormSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone_num', 'nickname']

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_num=validated_data['phone_num'],
            nickname=validated_data['nickname'],
        )
        return customer

    def validate(self, data):
        # Apply custom validation either here, or in the view.
        # print(data)
        return data
