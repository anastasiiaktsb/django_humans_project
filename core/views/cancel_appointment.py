from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from core.models import Appointment
from django_human_project.permissions import IsPatient

from core.tasks import send_email_on_appointment_cancel


class AppointmentCancelAPIView(UpdateAPIView):
    permission_classes = [IsPatient]
    model = Appointment

    def get_queryset(self):
        return self.model.objects.filter(patient=self.request.user.patient)

    def update(self, request, *args, **kwargs):
        appointment = self.get_object()
        appointment.reject()
        self.send_emails(appointment)
        return Response('Appointment was successfully canceled')

    @staticmethod
    def send_emails(appointment):
        emails = [appointment.doctor.user.email, appointment.patient.user.email]
        send_email_on_appointment_cancel.delay(appointment.appt_date, appointment.appt_time, emails)
