from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import despesasViewSet

router = DefaultRouter()
router.register(r'despesas', despesasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
