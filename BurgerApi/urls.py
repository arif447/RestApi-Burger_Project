from django.urls import path
from BurgerApi.views import UserProfileViewset, OrderViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserProfileViewset)
router.register(r'order', OrderViewset, basename='order')

urlpatterns = [
              path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
              path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
