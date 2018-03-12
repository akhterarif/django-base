from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from .managers import TagModelManager


class TagModel(BaseModel):
    """
    This is the model for Tag of a post
    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Tag Name'),
        help_text=_('Tag Name.'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{name}".format(name=self.name)

    objects = TagModelManager()

    class Meta:
        db_table = 'blog_tags'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
