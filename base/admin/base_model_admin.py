from django.contrib import admin

class BaseModelAdmin(admin.ModelAdmin):
    """
    This class is base admin class. Whish holds the methods
    and properties for common operations for admin.
    """
    list_display = ('id',
                    'uuid',)
    readonly_fields = ('date_created',
                       'date_updated',
                       'uuid',
                       'id',
                       'created_by',
                       'updated_by',
                       'deleted_by',)
    search_fields = ('id',
                     'uuid',)

    def save_model(self, request, obj, form, change):
        if obj.id:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
