from rest_framework import serializers
from core.models import Human


class HumanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Human
        fields = (
            'id', 'surname', 'age', 'gender',
            'number_of_teeth', 'number_of_surgeries',
        )
        read_only_fields = ('id', )
