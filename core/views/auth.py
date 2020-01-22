from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from core.serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
