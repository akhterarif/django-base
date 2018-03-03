from base.api.serializers import BaseModelSerializer
from ...models import PostModel

class PostModelSerializer(BaseModelSerializer):
	"""
	PostModelSerializer for post
	"""

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title')