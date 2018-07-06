from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from .managers import CategoryModelManager


class CategoryModel(BaseModel):
    """
    Give a description of the model here
    """
    name = name = models.CharField(
        max_length=128,
        verbose_name=_('Category Name'),
        help_text=_('Category Name.'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{model}-{id}'.format(model=CategoryModel, id=id)

    objects = CategoryModelManager()

    class Meta:
        db_table = 'blog_categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
