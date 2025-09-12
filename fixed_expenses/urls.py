from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FixedExpenseViewSet, FixedExpenseInstanceViewSet

router = DefaultRouter()
router.register(r'', FixedExpenseViewSet,
                basename='fixed-expense')
router.register(r'/instance', FixedExpenseInstanceViewSet,
                basename='fixed-instance')

urlpatterns = [
    path('', include(router.urls)),
]
