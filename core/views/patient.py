import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView

from django_human_project.permissions import IsPatient
from core.models import Doctor



class DoctorFilter(django_filters.rest_framework.FilterSet):
    surname = django_filters.CharFilter(lookup_expr="startswith")

    class Meta:
        model = Doctor
        fields = ['surname', 'gender', ]


class PatientDoctorsListAPIView(ListAPIView):
    permission_classes = (IsPatient, )
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, ]
    ordering_fields = ['surname', ]
    filter_class = DoctorFilter

    def get_queryset(self):
        doctor_ids = self.request.user.patient.appointments.all().values_list('doctor__id')
        return Doctor.objects.filter(id__in=doctor_ids)

