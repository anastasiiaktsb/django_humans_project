from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import serializers

from django_human_project import settings


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        subject = "Thanks for registering"
        message = f"Hello {user.username}. You're awesome! Thanks for registering."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [validated_data['email']])
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
