from base.api.views import BaseListAPIView
from ..serializers import CategoryModelSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet

class CategoryListAPIView(BaseListAPIView):
	"""
	CategoryListAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryModelSerializer
	filter_class = CategoryFilterSet

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)