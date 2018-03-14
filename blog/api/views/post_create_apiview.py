from base.api.views import BaseCreateAPIView
from ..serializers import PostCreateSerializer, PostOutputSerializer
from ...services import PostService
from ..filtersets import PostFilterSet
from rest_framework.permissions import IsAuthenticated

class PostCreateAPIView(BaseCreateAPIView):
	"""
	PostCreateAPIView for the project
	"""
	service_class = PostService
	serializer_class = PostCreateSerializer
	output_serializer = PostOutputSerializer
	filter_class = PostFilterSet
	permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)