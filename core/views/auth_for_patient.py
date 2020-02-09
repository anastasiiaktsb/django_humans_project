from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from core.serializers import PatientRegisterSerializer


class PatientRegisterAPIView(CreateAPIView):
    serializer_class = PatientRegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
