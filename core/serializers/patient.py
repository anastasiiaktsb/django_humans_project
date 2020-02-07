from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import serializers

from core.models import Patient
from django_human_project import settings


class PatientRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = Patient
        fields = (
            'username', 'email', 'password',
            'surname', 'gender', 'age',
            'number_of_teeth', 'number_of_surgeries',
        )

    def create(self, validated_data):
        username = serializers.CharField(source='user.username')
        email = serializers.EmailField(source='user.email')
        password = serializers.CharField(source='user.password')
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        patient = Patient.objects.create(user=user, **validated_data)
        if Patient.objects.filter(user__username=username).exists():
            raise serializers.ValidationError({'username': 'This username is reserved.'})
        subject = "Thanks for registering"
        message = f"Hello {user.username}. You're awesome! Thanks for registering."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'username', 'email', 'password', 'surname', 'gender', 'age', 'number_of_teeth',
                  'number_of_surgeries',)
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        patient = super().update(instance, validated_data)
        patient.user.set_password(password)
        patient.user.save()
        return patient
