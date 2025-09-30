from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FixedIncomeViewSet, FixedIncomeInstanceViewSet

router = DefaultRouter()
router.register(r'', FixedIncomeViewSet, basename='fixed-income')
router.register(r'', FixedIncomeInstanceViewSet,
                basename='fixed-income-instance')

urlpatterns = [
    path('', include(router.urls)),
]
