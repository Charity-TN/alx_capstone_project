from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, TransactionViewSet, TrackingViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'users', UserViewSet, basename='users')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'tracking', TrackingViewSet, basename='tracking')

urlpatterns = [
    path('', include(router.urls)),
]