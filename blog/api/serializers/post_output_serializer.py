from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import CategoryOutputSerializer, TagOutputSerializer

class PostOutputSerializer(BaseModelSerializer):
	"""
	PostModelSerializer for post
	"""
	category = CategoryOutputSerializer(read_only=True)
	tags = TagOutputSerializer(read_only=True, many=True)

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title', 'tags')