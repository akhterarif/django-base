from base.api.views import BaseUpdateAPIView
from ..serializers import TagUpdateSerializer, TagOutputSerializer
from ...services import TagService
from rest_framework.permissions import IsAuthenticated

class TagUpdateAPIView(BaseUpdateAPIView):
	"""
	TagUpdateAPIView for the project
	"""
	service_class = TagService
	serializer_class = TagUpdateSerializer
	output_serializer = TagOutputSerializer
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