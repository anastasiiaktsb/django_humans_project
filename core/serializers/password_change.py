from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserPasswordChangeSerializer(ModelSerializer):
    old_password = serializers.CharField(required=True, max_length=30, write_only=True)
    password = serializers.CharField(required=True, max_length=30, write_only=True)
    confirmed_password = serializers.CharField(required=True, max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'confirmed_password')

    def validate(self, data):
        user = self.instance
        if user:
            if not user.check_password(data.get('old_password')):
                raise serializers.ValidationError({'old_password': 'Wrong password.'})

            if data.get('confirmed_password') != data.get('password'):
                raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
