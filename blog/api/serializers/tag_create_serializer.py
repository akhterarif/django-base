from base.api.serializers import BaseModelSerializer
from ...models import TagModel

class TagCreateSerializer(BaseModelSerializer):
	"""
	TagCreateSerializer for tag
	"""

	class Meta:
		model = TagModel
		fields = ('name',)