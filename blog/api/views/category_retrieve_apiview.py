from base.api.views import BaseRetrieveAPIView
from ..serializers import CategoryOutputSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet
from rest_framework.permissions import IsAuthenticated

class CategoryRetrieveAPIView(BaseRetrieveAPIView):
	"""
	CategoryRetrieveAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryOutputSerializer
	filter_class = CategoryFilterSet
	permission_classes = (IsAuthenticated,)

	def retrieve(self, request, uuid, *args, **kwargs):
		return self.get(request, uuid=uuid, *args, **kwargs)