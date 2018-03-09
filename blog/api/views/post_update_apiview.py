from base.api.views import BaseUpdateAPIView
from ..serializers import PostUpdateSerializer, PostOutputSerializer
from ...services import PostService
from ..filtersets import PostFilterSet
from rest_framework.permissions import IsAuthenticated

class PostUpdateAPIView(BaseUpdateAPIView):
	"""
	PostUpdateAPIView for the project
	"""
	service_class = PostService
	serializer_class = PostUpdateSerializer
	output_serializer = PostOutputSerializer
	filter_class = PostFilterSet
	permission_classes = (IsAuthenticated,)

	def put(self,
			request,
			uuid,
			*args,
			**kwargs):
		return self.update(request,
						   uuid,
						   *args,
						   **kwargs)