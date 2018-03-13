from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import CategoryOutputSerializer, TagOutputSerializer


class PostCreateSerializer(BaseModelSerializer):
	"""
	PostCreateSerializer for post
	"""
	category = CategoryOutputSerializer(required=True)
	tags = TagOutputSerializer(many=True)

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title', 'tags')