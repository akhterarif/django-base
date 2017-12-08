from django.db import models
from base.models.managers import BaseManager


class CategoryManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super(CategoryManager, self).__init__(*args, **kwargs)
