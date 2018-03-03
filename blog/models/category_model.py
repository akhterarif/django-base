from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from .managers import CategoryModelManager


class CategoryModel(BaseModel):
    """
    This is the model for Category of the blog
    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Category Name'),
        help_text=_('Category Name.')
    )

    def __str__(self):
        return "{name}".format(name=self.name)

    objects = CategoryModelManager()

    class Meta:
        db_table = 'blog_categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
