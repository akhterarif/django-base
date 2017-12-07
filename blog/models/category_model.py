from django.conf import settings
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class CategoryModel(BaseModel):
    """
    This is the model for Category of the blog
    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Document Number'),
        help_text=_('User ID document number.'),
        null=True, blank=True
    )

    def __str__(self):
        return "{name}".format(name=self.name)

    # objects = UsersIDManager()

    class Meta:
        db_table = 'blog_categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
