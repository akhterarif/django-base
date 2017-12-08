from django.db import models
from ..managers import SoftDeletionManager


class BaseManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(BaseManager, self).__init__(*args, **kwargs)
