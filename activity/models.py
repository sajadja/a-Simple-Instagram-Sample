from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from content.models import Post
from lib.common_models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    caption = models.TextField(_('caption'))
    reply_to = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Like(BaseModel):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return '{} >> {}'.format(self.user.username, self.post.id)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')
