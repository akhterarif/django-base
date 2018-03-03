from base.admin import BaseModelAdmin

class PostAdmin(BaseModelAdmin):
    """
    This is admin for category
    """
    list_display = ('id',
                    'uuid',
                    'category',
                    'title',
                    'text',
                    'created_by',)
    readonly_fields = ('created_at',
                       'updated_at',
                       'deleted_at',
                       'uuid',
                       'id',
                       'created_by',
                       'updated_by',)
    search_fields = ('id',
                     'uuid',
                     'category__uuid',
                     'category__name',
                     'title',
                     'text',)
