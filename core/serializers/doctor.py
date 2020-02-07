from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import serializers

from core.models import Doctor
from django_human_project import settings


class DoctorRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ('username', 'email', 'password', 'surname', 'gender',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        username = serializers.CharField(source='user.username')
        email = serializers.EmailField(source='user.email')
        password = serializers.CharField(source='user.password')
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        doctor = Doctor.objects.create(user=user, **validated_data)
        if Doctor.objects.filter(user__username=username).exists():
            raise serializers.ValidationError({'username': 'This username is reserved.'})
        subject = "Thanks for registering"
        message = f"Hello {user.username}. You're awesome! Thanks for registering."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ('id', 'username', 'email', 'password', 'surname', 'gender',)
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        doctor = super().update(instance, validated_data)
        doctor.user.set_password(password)
        doctor.user.save()
        return doctor
