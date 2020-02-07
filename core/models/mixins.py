from django.db import models


class CreatedDateMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedDateMixin(models.Model):
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FindInDateRangeMixin:

    @classmethod
    def _find_in_date_range(cls, field, since=None, until=None):
        filter_params = {}
        field_name = field.field_name
        if since:
            filter_params[f'{field_name}__gte'] = since
        if until:
            filter_params[f'{field_name}__lte'] = until
        return cls.objects.filter(**filter_params)
