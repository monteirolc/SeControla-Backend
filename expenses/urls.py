from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseSerializer

router = DefaultRouter()
router.register(r'', ExpenseSerializer, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]
