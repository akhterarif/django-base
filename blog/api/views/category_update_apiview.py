from base.api.views import BaseUpdateAPIView
from ..serializers import CategoryUpdateSerializer, CategoryOutputSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet
from rest_framework.permissions import IsAuthenticated

class CategoryUpdateAPIView(BaseUpdateAPIView):
	"""
	CategoryUpdateAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryUpdateSerializer
	output_serializer = CategoryOutputSerializer
	filter_class = CategoryFilterSet
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