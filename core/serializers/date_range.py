from rest_framework import serializers


class DateRangeSerializer(serializers.Serializer):
    since = serializers.DateField()
    until = serializers.DateField()
