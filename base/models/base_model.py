import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from permissions.decorators import check_permission

from ..custom_exceptions import MissUseError
from ..utils import get_model_field_names
from .soft_deletion_model import SoftDeletionModel
# from .managers import


class BaseModel(SoftDeletionModel):
    """
    Base model for this project.

    Contains the base properties and methods for all models.
    """

    uuid = models.UUIDField(
        verbose_name=_('Unique Identifier'),
        help_text=_('Unique Identifier.'),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
        help_text=_('Keep this record active or not.')
    )
    is_archived = models.BooleanField(
        verbose_name=_('Is Archived'),
        default=False,
        help_text=_('Keep this record active or not.')
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Created By'),
        help_text=_('User Who Create This Record'),
        related_name='created_by',
        null=True, blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Updated By'),
        help_text=_('User Who Last Update This Record'),
        related_name='updated_by',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name=_('DateTime Created'),
        help_text=_('Creation Date.'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('DateTime Updated'),
        help_text=_('Last Update.'),
        auto_now=True,
    )

    class Meta:
        abstract = True
