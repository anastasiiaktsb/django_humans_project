from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from core.serializers.doctor import DoctorSerializer


class DoctorRegisterAPIView(CreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
