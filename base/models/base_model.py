import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .soft_deletion_model import SoftDeletionModel


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
        help_text=_('User Who Created This Record'),
        related_name='created_by',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Updated By'),
        help_text=_('User Who Last Updated This Record'),
        related_name='updated_by',
        null=True, blank=True,
        on_delete=models.CASCADE,
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

    def _check_permission(self,
                          user,
                          permission,
                          model):
        """
        Checks the permission of a user in a model
        :param user: who's permission have to be checked
        :param permission: name of the permission like 'add', change
        :param model: which model's permission has to check

        :return: Boolean value
        """
        permission_name = ''
        permission_name = "{permission}_{model}".format(
            permission=permission,
            model=model.to_lower())
        return getattr(user, permission_name)

    def _created_at(self):
        return self.created_at.isoformat()

    def _update_at(self):
        return self.updated_at.isoformat()

    created_datetime = property(_created_at)
    updated_datetime = property(_update_at)

    class Meta:
        abstract = True
