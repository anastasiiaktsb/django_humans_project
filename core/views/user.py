from rest_framework.generics import RetrieveUpdateAPIView

from core.serializers import UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
