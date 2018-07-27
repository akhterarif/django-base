from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models.base_model import BaseModel
from .managers import TestModelManager



class TestModel(BaseModel):
    """
    Give a description of the model here
    """

    def __str__(self):
        return "TestModel-id".format(model=TestModel, id=id)

    objects = TestModelManager()

    class Meta:
        db_table = 'blog_tests'
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')
