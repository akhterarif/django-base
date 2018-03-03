from base.api.serializers import BaseModelSerializer
from ...models import CategoryModel

class CategoryModelSerializer(BaseModelSerializer):
	"""
	CategoryModelSerializer for category
	"""
	def __init__(self):
		super(CategoryModelSerializer, self).__init__()

	class Meta:
		model = CategoryModel
		fields = ('name')