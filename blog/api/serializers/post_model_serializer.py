from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import CategoryModelSerializer

class PostModelSerializer(BaseModelSerializer):
	"""
	PostModelSerializer for post
	"""
	category = CategoryModelSerializer(read_only=True)

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title')