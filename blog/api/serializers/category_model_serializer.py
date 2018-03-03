from base.api.serializers import BaseModelSerializer
from ...models import CategoryModel

class CategoryModelSerializer(BaseModelSerializer):
	"""
	CategoryModelSerializer for category
	"""

	class Meta:
		model = CategoryModel
		fields = ('uuid', 'name')