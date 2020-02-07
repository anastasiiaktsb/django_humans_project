from django.db import models

# from core.models import Doctor, Patient
from core.models.mixins import CreatedDateMixin, UpdatedDateMixin, FindInDateRangeMixin


class Appointment(
    FindInDateRangeMixin,
    CreatedDateMixin,
    UpdatedDateMixin,
    models.Model,
):
    PENDING = 1
    REJECTED = 2
    FINISHED = 3
    ORDER_STATUS = (
        (PENDING, "Pending"),
        (REJECTED, "Rejected"),
        (FINISHED, "Finished")
    )
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS, default=PENDING)
    appt_date = models.DateField()
    appt_time = models.TimeField()
    doctor = models.ForeignKey(related_name='appointments', on_delete=models.CASCADE, to='core.Doctor')
    patient = models.ForeignKey(related_name='appointments', on_delete=models.CASCADE, to='core.Patient')

    def __str__(self):
        return f'Appointment(id={self.id}, status={self.status})'

    def reject(self):
        self.status = self.REJECTED
        self.save()

    @classmethod
    def find_in_date_range(cls, since=None, until=None):
        return cls._find_in_date_range(cls.appt_date, since, until)
