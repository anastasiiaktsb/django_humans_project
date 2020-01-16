from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import (
    UserRegisterAPIView,
    UserRetrieveUpdateAPIView,
    HumanViewSet,
)

router = routers.DefaultRouter()
router.register(r'humans', HumanViewSet, basename='humans')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('me/', UserRetrieveUpdateAPIView.as_view(), name='user-info'),
]
