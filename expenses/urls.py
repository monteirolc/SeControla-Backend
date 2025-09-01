from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseSerializer

router = DefaultRouter()
router.register(r'incomes', ExpenseSerializer, basename='income')

urlpatterns = [
    path('', include(router.urls)),
]
