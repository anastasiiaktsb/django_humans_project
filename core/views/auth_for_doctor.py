from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from core.serializers import DoctorRegisterSerializer


class DoctorRegisterAPIView(CreateAPIView):
    serializer_class = DoctorRegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
