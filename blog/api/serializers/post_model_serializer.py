from base.api.serializers import BaseModelSerializer
from ...models import PostModel

class PostModelSerializer(BaseModelSerializer):
	"""
	CategoryModelSerializer for category
	"""

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title')