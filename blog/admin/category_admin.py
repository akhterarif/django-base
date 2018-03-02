from base.admin import BaseModelAdmin

from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _


class CategoryAdmin(BaseModelAdmin):
    """
    This is admin for category
    """
    list_display = ('id',
                    'uuid',
                    'name')
    readonly_fields = ('created_at',
                       'updated_at',
                       'deleted_at',
                       'uuid',
                       'id',
                       'created_by',
                       'updated_by',)
    search_fields = ('id',
                     'uuid',
                     'name')
