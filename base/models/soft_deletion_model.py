from django.db import models
from .managers import SoftDeletionManager


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(
        verbose_name=_('DateTime Updated'),
        help_text=_('Deleted Time'),
        blank=True, null=True
    )

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()
