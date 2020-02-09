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
        user_info = validated_data.pop('user')
        user = User(username=user_info['username'], email=user_info['email'])
        user.set_password(user_info['password'])
        user.save()
        patient = Patient.objects.create(user=user, **validated_data)
        subject = "Thanks for registering"
        message = f"Hello {user.username}. You're awesome! Thanks for registering."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        return patient

    def validate(self, attrs):
        if Patient.objects.filter(user__username=attrs['user']['username']).exists():
            raise serializers.ValidationError({'username': 'This username is reserved.'})
        return attrs


class PatientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', required=True)
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = Patient
        fields = ('id', 'username', 'email', 'password', 'surname', 'gender', 'age', 'number_of_teeth',
                  'number_of_surgeries',)
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

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
