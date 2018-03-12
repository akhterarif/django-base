from base.api.views import BaseCreateAPIView
from ..serializers import TagCreateSerializer, TagOutputSerializer
from ...services import TagService
from rest_framework.permissions import IsAuthenticated

class TagCreateAPIView(BaseCreateAPIView):
	"""
	TagCreateAPIView for the project
	"""
	service_class = TagService
	serializer_class = TagCreateSerializer
	output_serializer = TagOutputSerializer
	permission_classes = (IsAuthenticated,)

	def post(self,
			 request,
			 *args,
			 **kwargs):
		return self.create(request,
						   *args,
						   **kwargs)