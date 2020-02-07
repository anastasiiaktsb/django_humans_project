import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from django_human_project.permissions import IsDoctor
from core.models import Patient


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         user = self.request.user
#         if hasattr(user, 'patient'):
#             return user.patient.all()
#         return user.doctor.all()


class PatientFilter(django_filters.rest_framework.FilterSet):
    surname = django_filters.CharFilter(lookup_expr="startswith")

    class Meta:
        model = Patient
        fields = ['surname', 'age', 'gender', 'number_of_teeth', 'number_of_surgeries', ]


class DoctorPatientsListAPIView(ListAPIView):
    permission_classes = (IsDoctor, )
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, ]
    ordering_fields = ['surname', 'age', 'number_of_teeth', 'number_of_surgeries', ]
    filter_class = PatientFilter

    def get_queryset(self):
        patient_ids = self.request.user.doctor.appointments.all().values_list('patient__id')
        return Patient.objects.filter(id__in=patient_ids)
