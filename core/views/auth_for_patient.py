from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from core.serializers.patient import PatientSerializer


class PatientRegisterAPIView(CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
