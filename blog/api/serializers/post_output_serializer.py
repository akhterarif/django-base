from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import Cat

class PostOutputSerializer(BaseModelSerializer):
	"""
	PostModelSerializer for post
	"""
	category = CategoryModelSerializer(read_only=True, many=True)

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title')