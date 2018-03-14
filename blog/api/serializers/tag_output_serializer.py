from base.api.serializers import BaseModelSerializer
from ...models import TagModel

class TagOutputSerializer(BaseModelSerializer):
	"""
	TagOutputSerializer for tag
	"""

	class Meta:
		model = TagModel
		fields = ('uuid', 'name',)