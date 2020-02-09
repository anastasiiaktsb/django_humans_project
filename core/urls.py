from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import (
    DoctorRegisterAPIView,
    PatientRegisterAPIView,
    APIChangePasswordView,
    AppointmentCancelAPIView,
    DoctorPatientsListAPIView,
    PatientDoctorsListAPIView,
    AppointmentsListAPIView,
    UserRetrieveUpdateAPIView,
)

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('register-for-doctor/', DoctorRegisterAPIView.as_view(), name='doctor-register'),
    path('register-for-patient/', PatientRegisterAPIView.as_view(), name='patient-register'),

    path('me/', UserRetrieveUpdateAPIView.as_view(), name='user-info'),
    path('reset-password/', APIChangePasswordView.as_view(), name='reset-password'),

    path('appointments/<pk>/cancel/', AppointmentCancelAPIView.as_view(), name='cancel-appointment'),

    path('patients/', DoctorPatientsListAPIView.as_view(), name='doctor-patients'),

    path('doctors/', PatientDoctorsListAPIView.as_view(), name='patient-doctors'),

    path('appointments/', AppointmentsListAPIView.as_view(), name='appointments'),
]
