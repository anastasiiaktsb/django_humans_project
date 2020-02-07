from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import models, User


class Patient(models.Model):
    GENDER_CHOICES = (
        (1, "Male"),
        (2, "Female"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    number_of_teeth = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(32)]
    )
    number_of_surgeries = models.PositiveIntegerField()

    def __str__(self):
        return f'Patient(id={self.id}, email={self.email})'
