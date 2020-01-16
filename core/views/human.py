import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from core.models import Human
from core.serializers.human import HumanSerializer


class HumanFilter(django_filters.rest_framework.FilterSet):
    surname = django_filters.CharFilter(lookup_expr="startswith")

    class Meta:
        model = Human
        fields = ['surname', 'age', 'gender', 'number_of_teeth', 'number_of_surgeries',]


class HumanViewSet(viewsets.ModelViewSet):
    serializer_class = HumanSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, ]
    ordering_fields = ['surname', 'age', 'number_of_teeth', 'number_of_surgeries',]
    filter_class = HumanFilter

    def get_queryset(self):
        return self.request.user.humans.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
