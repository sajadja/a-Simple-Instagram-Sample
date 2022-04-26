from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lib.common_models import BaseModel


class Location(BaseModel):
    title = models.CharField(_('title'), max_length=32)
    points = models.JSONField(_('points'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')
