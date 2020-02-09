from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.serializers import AppointmentSerializer, DateRangeSerializer
from core.models import Appointment


class AppointmentsListAPIView(ListAPIView):
    model = Appointment
    permission_classes = (IsAuthenticated, )
    serializer_class = AppointmentSerializer
    params_serializer = DateRangeSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return user.patient.appointments.all()
        return user.doctor.appointments.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        if not hasattr(self.request.user, 'doctor'):
            return queryset
        serializer = self.params_serializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        return self.model.find_in_date_range(serializer.data)
