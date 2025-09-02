from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharedAccountViewSet

router = DefaultRouter()
router.register(r'shared-accounts', SharedAccountViewSet,
                basename='shared-account')

urlpatterns = [
    path('', include(router.urls)),
]
