from base.api.serializers import BaseModelSerializer
from ...models import TagModel

class TagUpdateSerializer(BaseModelSerializer):
	"""
	TagUpdateSerializer for tag
	"""

	class Meta:
		model = TagModel
		fields = ('name',)