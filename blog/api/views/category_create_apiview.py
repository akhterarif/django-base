from base.api.views import BaseCreateAPIView
from ..serializers import CategoryCreateSerializer, CategoryOutputSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet
from rest_framework.permissions import IsAuthenticated

class CategoryCreateAPIView(BaseCreateAPIView):
	"""
	CategoryCreateAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryCreateSerializer
	output_serializer = CategoryOutputSerializer
	filter_class = CategoryFilterSet
	permission_classes = (IsAuthenticated,)

	def post(self,
			 request,
			 *args,
			 **kwargs):
		return self.create(request,
						   *args,
						   **kwargs)