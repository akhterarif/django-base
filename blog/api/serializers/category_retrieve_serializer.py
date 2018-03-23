from base.api.serializers import BaseModelSerializer
from ...models import CategoryModel

class CategoryRetrieveSerializer(BaseModelSerializer):
	"""
	CategoryRetrieveSerializer for category
	"""

	class Meta:
		model = CategoryModel
		fields = ('uuid', 'name',)