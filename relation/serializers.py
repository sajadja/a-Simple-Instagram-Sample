from rest_framework import serializers

from relation.models import Relation
from user.api.serializers import UserLightsSerializers


class FollowersSerializers(serializers.ModelSerializer):
    from_user = UserLightsSerializers()
    followed_back = serializers.SerializerMethodField()

    class Meta:
        model = Relation
        fields = ['from_user', 'followed_back', 'created_time']

    def get_followed_back(self, obj):
        return Relation.objects.filter(from_user=obj.to_user, to_user=obj.from_user).exists()
