from rest_framework import serializers

from location.models import Location


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['title', 'points']
