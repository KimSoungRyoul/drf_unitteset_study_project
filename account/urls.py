from rest_framework import routers

from account.views import CustomerAPIViewSet

customer_router = routers.SimpleRouter()
customer_router.register('customer', viewset=CustomerAPIViewSet)

urlpatterns = []

urlpatterns += customer_router.urls
