from base.api.serializers import BaseModelSerializer
from ...models import CategoryModel

class CategoryCreateSerializer(BaseModelSerializer):
	"""
	CategoryCreateSerializer for category
	"""

	class Meta:
		model = CategoryModel
		fields = ('name',)