from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from activity.models import Comment
from relation.models import Relation


class CreateCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'caption', 'reply_to']

    def validate(self, attrs):
        request = self.context['request']

        if attrs['reply_to'] is not None and attrs['reply_to'].post != attrs['post']:
            raise ValidationError(_('post and replay to comment post are not the same'))

        if attrs['post'].user != request.user and not Relation.objects.filter(
                from_user=request.user, to_user=attrs['post'].user).exists():
            raise ValidationError(_('you are not following the user of post owner'))

        return attrs


class ListCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'caption', 'reply_to']
