from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Human(models.Model):
    GENDER_CHOICES = (
        (1, "Male"),
        (2, "Female"),
    )

    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    number_of_teeth = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(32)]
    )
    number_of_surgeries = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='humans')

    def __str__(self):
        return f'Human(id={self.id}, surname={self.surname})'
