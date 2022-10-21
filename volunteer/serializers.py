from rest_framework import serializers
from .models import VolunteerType


class VolunteerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerType
        fields = ('pk', 'name', 'restricted', 'description', 'requires_driver_license', 'url')
