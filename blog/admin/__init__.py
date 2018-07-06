from django.contrib import admin

from ..models import CategoryModel

from .category_admin import CategoryAdmin

admin.site.register(CategoryModel, CategoryAdmin)
