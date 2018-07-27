from django.contrib import admin

from ..models import CategoryModel, PostModel

from .category_admin import CategoryAdmin
from .post_admin import PostAdmin

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(PostModel, PostAdmin)
