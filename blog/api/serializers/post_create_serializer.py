from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import CategoryModelSerializer


class PostCreateSerializer(BaseModelSerializer):
	"""
	PostCreateSerializer for post
	"""
	category = CategoryModelSerializer(required=True, many=True)

	class Meta:
		model = PostModel
		fields = ('uuid', 'category', 'text', 'title')