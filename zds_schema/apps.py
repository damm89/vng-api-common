from django.apps import AppConfig
from django.db import models

from drf_yasg import openapi
from drf_yasg.inspectors.field import (
    model_field_to_basic_type, serializer_field_to_basic_type,
    basic_type_info
)
from rest_framework import serializers


class ZDSSchemaConfig(AppConfig):
    name = 'zds_schema'

    def ready(self):
        patch_duration_type()


def patch_duration_type():

    def _patch(basic_types, _field_cls):
        for index, (field_cls, basic_type) in enumerate(basic_types):
            if field_cls is _field_cls:
                basic_types[index] = (_field_cls, (openapi.TYPE_STRING, None))
                break

    _patch(model_field_to_basic_type, models.DurationField)
    _patch(basic_type_info, models.DurationField)
    _patch(serializer_field_to_basic_type, serializers.DurationField)
    _patch(basic_type_info, serializers.DurationField)
