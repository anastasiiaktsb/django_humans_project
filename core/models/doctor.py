from django.contrib.auth.models import User, models
from core.models.mixins import CreatedDateMixin, UpdatedDateMixin


class Doctor(
    CreatedDateMixin,
    UpdatedDateMixin,
    models.Model,
):
    GENDER_CHOICES = (
        (1, "Male"),
        (2, "Female"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return f'Doctor(id={self.id}, surname={self.surname}, email={self.user.email})'
