from base.api.views import BaseListAPIView
from ..serializers import PostModelSerializer
from ...services import PostService
from ..filtersets import PostFilterSet

class PostListAPIView(BaseListAPIView):
	"""
	PostListAPIView for the project
	"""
	service_class = PostService
	serializer_class = PostModelSerializer
	filter_class = PostFilterSet

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)