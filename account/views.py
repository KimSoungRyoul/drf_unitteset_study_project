# Create your views here.
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import mixins

from account.documents import DjangoFilterDescriptionInspector
from account.models import Customer
from account.serializers import CustomerInfoSerializer, SignUpFormSerializer


@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="회원 개인정보 조회 API",
    filter_inspectors=[DjangoFilterDescriptionInspector],
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="회원 가입 API",
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="회원 정보 수정 API",
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="회원 탈퇴 API",
))
class CustomerAPIViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset: QuerySet = Customer.objects
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SignUpFormSerializer
        elif self.request.method == 'GET':
            return CustomerInfoSerializer
        elif self.request.method == 'PUT':
            return SignUpFormSerializer
        elif self.request.method == 'DELETE':
            return SignUpFormSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED, headers=headers)
