from base.api.views import BaseListAPIView
from ..serializers import TagOutputSerializer
from ...services import TagService
from ..filtersets import TagFilterSet
from rest_framework.permissions import IsAuthenticated

class TagListAPIView(BaseListAPIView):
	"""
	TagListAPIView for the project
	"""
	service_class = TagService
	serializer_class = TagOutputSerializer
	filter_class = TagFilterSet
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)