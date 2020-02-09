from rest_framework.generics import RetrieveUpdateAPIView

from core.serializers import DoctorSerializer
from core.serializers import PatientSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    def get_serializer_class(self):
        if hasattr(self.request.user, 'patient'):
            return PatientSerializer
        return DoctorSerializer

    def get_object(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return user.patient
        return user.doctor
