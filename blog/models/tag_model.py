from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models.base_model import BaseModel
from .managers.tag_model_manager import TagModelManager


class TagModel(BaseModel):
    """
    Give a description of the model here
    """

    name = name = models.CharField(
        max_length=128,
        verbose_name=_('Tag Name'),
        help_text=_('Tag Name.'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return "TagModel-id".format(model=TagModel, id=id)

    objects = TagModelManager()

    class Meta:
        db_table = 'blog_tags'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
