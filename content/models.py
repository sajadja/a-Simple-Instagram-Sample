from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lib.common_models import BaseModel
from location.models import Location

User = get_user_model()


class Post(BaseModel):
    caption = models.TextField(_('caption'), blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.user.username, self.id)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, _('image')),
        (VIDEO, _('video'))
    )
    media_type = models.PositiveSmallIntegerField(_('media type'), choices=TYPE_CHOICES, default=IMAGE)
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_file = models.FileField(
        _('media file'), upload_to='content/media/',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg', 'mp4', 'wmv', 'flv'))]
    )

    def __str__(self):
        return '{} - {}'.format(str(self.post), self.get_media_type_display())

    class Meta:
        verbose_name = _('media')
        verbose_name_plural = _('media')


class Tag(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name='hashtags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return '{} > ({})'.format(self.tag, self.post)

    class Meta:
        verbose_name = _('postTag')
        verbose_name_plural = _('postTags')


class TaggedUser(BaseModel):
    post = models.ForeignKey(Post, related_name='tagged_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tagged_posts', on_delete=models.CASCADE)

    def __str__(self):
        return '{} > ({})'.format(self.user, self.post)

    class Meta:
        verbose_name = _('taggedUser')
        verbose_name_plural = _('taggedUsers')
