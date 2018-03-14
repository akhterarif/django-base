from base.api.serializers import BaseModelSerializer
from ...models import CategoryModel

class CategoryUpdateSerializer(BaseModelSerializer):
	"""
	CategoryUpdateSerializer for category
	"""

	class Meta:
		model = CategoryModel
		fields = ('name',)