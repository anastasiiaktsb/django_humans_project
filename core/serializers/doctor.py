from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import serializers

from core.models import Doctor
from django_human_project import settings


class DoctorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email', required=True)
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = Doctor
        fields = ('username', 'email', 'password', 'surname', 'gender',)

    def create(self, validated_data):
        user_info = validated_data.pop('user')
        user = User(username=user_info['username'], email=user_info['email'])
        user.set_password(user_info['password'])
        user.save()
        doctor = Doctor.objects.create(user=user, **validated_data)
        subject = "Thanks for registering"
        message = f"Hello {user.username}. You're awesome! Thanks for registering."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        return doctor

    def validate(self, attrs):
        if Doctor.objects.filter(user__username=attrs['user']['username']).exists():
            raise serializers.ValidationError({'username': 'This username is reserved.'})
        return attrs


class DoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', required=True)
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'username', 'email', 'password', 'surname', 'gender',)
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        user_info = validated_data.pop('user', {})
        email = user_info.get('email')
        validated_data.pop('password', None)
        user = instance.user
        if email and email != user.email:
            user.email = email
            user.save()
        instance = super().update(instance, validated_data)
        return instance
