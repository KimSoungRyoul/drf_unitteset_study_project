"""configuration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

swagger_info = openapi.Info(
    title="DRF 스터디 프로젝트",
    default_version='v1',
    description="Test description",
    terms_of_service="https://github.com/KimSoungRyoul/drf_unitteset_study_project",
    contact=openapi.Contact(email="KimSoungRyoul@gmail.com"),
    license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
    swagger_info,
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/v1/account/', include('account.urls')),

]
