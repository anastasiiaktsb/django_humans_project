from rest_framework.generics import UpdateAPIView

from core.serializers.password_change import UserPasswordChangeSerializer
from django_human_project.permissions import IsLoggedInUserOrAdmin


class APIChangePasswordView(UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    permission_classes = (IsLoggedInUserOrAdmin,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data = {'Password was successfully modified'}
        return response
