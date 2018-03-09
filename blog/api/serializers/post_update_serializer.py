from base.api.serializers import BaseModelSerializer
from ...models import PostModel
from ..serializers import CategoryOutputSerializer


class PostUpdateSerializer(BaseModelSerializer):
	"""
	PostUpdateSerializer for post
	"""
	category = CategoryOutputSerializer(required=True, many=True)

	class Meta:
		model = PostModel
		fields = ('category', 'text', 'title')