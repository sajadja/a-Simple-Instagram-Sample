from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserLightsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'bio', 'avatar', 'is_verified']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'bio', 'website', 'avatar', 'is_verified']
