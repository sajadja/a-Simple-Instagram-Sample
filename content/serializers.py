from rest_framework import serializers

from content.models import Post, PostMedia, PostTag, TaggedUser, Tag
from location.serializers import LocationSerializers
from user.api.serializers import UserLightsSerializers


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['media_type', 'media_file']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']


class HashTagsSerializers(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = PostTag
        fields = ['tag']


class TaggedUserSerializer(serializers.ModelSerializer):
    user = UserLightsSerializers()

    class Meta:
        model = TaggedUser
        fields = ['user']


class PostSerializers(serializers.ModelSerializer):
    user = UserLightsSerializers()
    location = LocationSerializers()
    media = PostMediaSerializer(many=True)
    hashtags = HashTagsSerializers(many=True)
    tagged_users = TaggedUserSerializer(many=True)

    class Meta:
        model = Post
        # TODO: show like and comment count
        fields = ['id', 'caption', 'user', 'location', 'media', 'hashtags', 'tagged_users']
